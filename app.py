from fastapi.responses import HTMLResponse, UJSONResponse
from mediaFire import Media
from fastapi import FastAPI, Request

app = FastAPI()
media = Media()

@app.get('/')
async def index():
    return HTMLResponse(content='Hello, world!', status_code=200)

@app.get('/get')
async def home(request: Request):
    id = request.query_params.get('id')

    if not id:
        data = {'status': False, 'message': 'id parameter is required'}
        return UJSONResponse(content=data, status_code=400)

    trans = await media.init(id)
    if trans['status']:
        return UJSONResponse(content=trans, status_code=200)
    return UJSONResponse(content=trans, status_code=404)

if __name__ == '__main__':
    import uvicorn
    config = uvicorn.Config(
        app="app:app",
        host="0.0.0.0",
        port=8000,
        workers=4,
        log_level="warning"
    )

    server = uvicorn.Server(config)
    server.run()