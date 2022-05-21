from pydantic import BaseModel
from app.schemas.form_schema import FormSchema


class AnswerFieldSchema(BaseModel):
    id: int
    value: str

    class Config:
        orm_mode = True


class AnswerResponseSchema(BaseModel):
    uid: str | None
    answers: list[AnswerFieldSchema]


class FormAnswersResponseSchema(BaseModel):
    answers: list[list[AnswerFieldSchema]]
    form_data: FormSchema


class AnswerFormSchema(BaseModel):
    uid: str
    answers: list[AnswerFieldSchema]

    class Config:
        orm_mode = True
