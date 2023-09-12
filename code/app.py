import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from code.config import TORTOISE_ORM
from code.handlers import create_cat, get_cats, get_cat, delete_cat, update_cat
from code.serializers import Cat

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.add_api_route('/cat/', create_cat, methods=['post'])
app.add_api_route('/cat/', get_cats, methods=['get'])  # , response_model=Cat
app.add_api_route('/cat/{cat_id}/', get_cat, methods=['get'])
app.add_api_route('/cat/{cat_id}/', delete_cat, methods=['delete'])
app.add_api_route('/cat/{cat_id}/', update_cat, methods=['put'])

register_tortoise(app, config=TORTOISE_ORM)
