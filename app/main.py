from fastapi import FastAPI
from app.router.form_router import api_v1
from fastapi.middleware.cors import CORSMiddleware

tags_metadata = [
    {
        'name': 'form',
        'description': 'Operations with forms.',
    },
    {
        'name': 'answer',
        'description': 'Operations with form answers.',
    },
]
app = FastAPI(
    docs_url='/',
    title='Form Constructor',
    description='Backend app for form constructor https://form-constructor-react.herokuapp.com/',
    version='0.0.1',
    contact={
        'name': 'Radin Gleb',
        'email': 'fc+gleb.rad@gmail.com',
    },
    openapi_tags=tags_metadata,
)


app.include_router(api_v1)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
