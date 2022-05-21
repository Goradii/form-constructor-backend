from typing import Type
from app.models.form_model import async_session
from app.dals.base_dal import BaseDAL


def get_dal(dal: Type[BaseDAL]):
    async def factory():
        async with async_session() as session:
            async with session.begin():
                yield dal(session)
    return factory
