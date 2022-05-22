from fastapi import Depends
from fastapi_jsonrpc import Entrypoint

from app.schemas.form_schema import FormSchema
from app.dals.form_dal import FormDAL
from app.dals.answer_dal import AnswerDAL
from app.schemas.answer_schema import AnswerFormSchema, AnswerResponseSchema
from app.depends.dependencies import get_dal

api_v1 = Entrypoint('/jrpc/v1/forms')


@api_v1.method()
async def new_form(form_data: FormSchema, form_dal: FormDAL = Depends(get_dal(FormDAL))) -> str:
    uid = await form_dal.new(form_data)
    return uid


@api_v1.method()
async def show_form(uid: str, form_dal: FormDAL = Depends(get_dal(FormDAL))) -> FormSchema:
    form = await form_dal.get_one(uid)
    return form


@api_v1.method()
async def submit_form(data: AnswerFormSchema, answer_dal: AnswerDAL = Depends(get_dal(AnswerDAL))) -> str:
    answer = await answer_dal.new(data)
    return answer


@api_v1.method()
async def show_answers_by_form(
        form_uid: str,
        answer_dal: AnswerDAL = Depends(get_dal(AnswerDAL)),
) -> list[AnswerResponseSchema]:
    answers = await answer_dal.get_by_form(form_uid)
    return answers


@api_v1.method()
async def show_answer(
        uid: str,
        answer_dal: AnswerDAL = Depends(get_dal(AnswerDAL)),
) -> AnswerResponseSchema:
    answers = await answer_dal.get_one(uid)
    return answers
