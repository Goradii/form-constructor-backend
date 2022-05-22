import fastapi_jsonrpc as jsonrpc
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
app = jsonrpc.API(
    docs_url='/',
    title='Form Constructor',
    description='Backend app for form constructor https://form-constructor-react.herokuapp.com/',
    version='0.0.1',
    contact={
        'name': 'Radin Gleb',
        'email': 'fc+gleb.rad@gmail.com',
    },
    openapi_tags=tags_metadata
)

app.bind_entrypoint(api_v1)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app.main:app', port=8888, access_log=True)
