from pydantic import BaseModel


class FieldBaseSchema(BaseModel):
    id: int
    type: str
    title: str
    description: str

    class Config:
        extra = 'forbid'


class InputBaseSchema(FieldBaseSchema):
    placeholder: str | None = None


class SelectOptionSchema(BaseModel):
    id: int
    value: str


class SelectBaseSchema(FieldBaseSchema):
    items: list[SelectOptionSchema]


class FormSchema(BaseModel):
    title: str
    description: str
    fields: list[InputBaseSchema | SelectBaseSchema]

    class Config:
        extra = 'forbid'
        orm_mode = True
