from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from mediaFire import Media
from json import loads
from dotenv import load_dotenv
from os import environ

load_dotenv()

CONTACTS = environ['CONTACTS']

app = FastAPI(
    title='MediaFire',
    description='This REST API receives the media ID and returns the download URL.',
    redoc_url='/',
    contact=loads(CONTACTS),
)

media = Media()

class ApiRequest(BaseModel):
    id: str

class ApiSuccess(BaseModel):
    name: str
    link: str

class ApiError(BaseModel):
    message: str

api_router = APIRouter(prefix="/api")

@api_router.post(
    '/media',
    responses={
        200: {"description": "Success", "model": ApiSuccess},
        404: {"description": "ID not found", "model": ApiError},
        400: {"description": "ID parameter not found", "model": ApiError},
    }
)
async def get_url(data: ApiRequest):
    if not data.id:
        raise HTTPException(status_code=400, detail="ID parameter is required")

    trans = await media.init(data.id)

    if trans.get('status'):
        return ApiSuccess(name=trans['message']['name'], link=trans['message']['link'])
    
    raise HTTPException(status_code=404, detail=trans.get('message', 'Unknown error'))

app.include_router(api_router)

if __name__ == '__main__':
    from uvicorn import run
    run(app="app:app", host="0.0.0.0", port=8000, log_level='warning')