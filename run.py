import uvicorn

if __name__ == '__main__':
    uvicorn.run('app.main:app', port=8888, access_log=True)
