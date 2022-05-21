import fastapi_jsonrpc as jsonrpc
from app.router.form_router import api_v1
from fastapi.middleware.cors import CORSMiddleware


app = jsonrpc.API(docs_url="/", redoc_url=None)

app.bind_entrypoint(api_v1)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["post"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app.main:app', port=5000, access_log=False)
