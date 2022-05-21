from app.dals.base_dal import BaseDAL
from app.models.form_model import Form

from app.schemas.form_schema import FormSchema
from sqlalchemy.future import select
from sqlalchemy.engine.result import ChunkedIteratorResult as Result
from uuid import uuid4


class FormDAL(BaseDAL):

    async def get_all(self, limit: int, offset: int) -> tuple[FormSchema]:
        query = select(Form)
        query_response: Result = await self.db_session.execute(query)
        return query_response.scalars().all()

    async def new(self, form: FormSchema) -> str:
        uid = await self._new_uid()
        new_form = Form(uid=uid, schema=form.dict())
        self.db_session.add(new_form)
        await self.db_session.flush()
        return uid

    async def get_one(self, uid):
        query = select(Form.schema).where(Form.uid == uid)
        query_response: Result = await self.db_session.execute(query)
        return query_response.scalars().one()

    async def _new_uid(self):
        query_result: Result = await self.db_session.execute(select(Form.uid))
        ids = set(query_result.scalars().all())
        uid = uuid4().hex
        while uid in ids:
            uid = uuid4().hex
        return uid
