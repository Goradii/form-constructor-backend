from app.dals.base_dal import BaseDAL
from app.models.form_model import Answer
from app.schemas.answer_schema import AnswerFormSchema
from sqlalchemy import select
from sqlalchemy.engine.result import ChunkedIteratorResult as Result
from uuid import uuid4


class AnswerDAL(BaseDAL):

    async def get_one(self, uid):
        query = select(Answer.answer_data).where(Answer.uid == uid)
        answers: Result = await self.db_session.execute(query)
        answers = answers.scalars().one()
        return answers

    async def get_by_form(self, form_uid):
        query = select(Answer.answer_data, Answer.uid).where(Answer.form_uid == form_uid)
        raw_answers: Result = await self.db_session.execute(query)
        raw_answers = raw_answers.fetchall()
        answers = []
        for answer in raw_answers:
            answers.append({**answer.answer_data, 'uid': answer.uid})
        return answers

    async def new(self, answer: AnswerFormSchema):
        uid = await self._new_uid()
        new_answer = Answer(uid=uid, answer_data=answer.dict(exclude={'uid'}), form_uid=answer.uid)
        self.db_session.add(new_answer)
        await self.db_session.flush()
        return uid

    async def _new_uid(self):
        query = await self.db_session.execute(select(Answer.uid))
        ids = set(query.scalars().all())
        uid = uuid4().hex
        while uid in ids:
            uid = uuid4().hex
        return uid
