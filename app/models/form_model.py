import os
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

CURRENT_TIMESTAMP = 'CURRENT_TIMESTAMP'
SA_CONNECTION_STRING = os.getenv('SA_CONNECT_STRING', 'sqlite+aiosqlite:///../db/forms_constructor.db')

engine = create_engine(SA_CONNECTION_STRING)
async_engine = create_async_engine(
    SA_CONNECTION_STRING,
    echo=False,
)
async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()


class Form(Base):
    __tablename__ = 'forms'
    uid = sa.Column(sa.Text(), primary_key=True, index=True)
    created_at = sa.Column(sa.DateTime(timezone=True), server_default=sa.text(CURRENT_TIMESTAMP))
    schema = sa.Column(sa.JSON())
    answers = relationship('Answer', back_populates='form')


class Answer(Base):
    __tablename__ = 'answers'
    uid = sa.Column(sa.Text, primary_key=True, index=True)
    answered_at = sa.Column(sa.DateTime(timezone=True), server_default=sa.text(CURRENT_TIMESTAMP))
    form_uid = sa.Column(sa.ForeignKey('forms.uid'))
    answer_data = sa.Column(sa.JSON())
    form = relationship(Form.__name__, back_populates='answers')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
