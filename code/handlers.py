import random
from datetime import datetime

from fastapi import Response, status
from tortoise.exceptions import DoesNotExist

from code.models import Cat
from code.constants import cat_names

async def create_cat(data: dict):
    cat_name = data.get('name') or random.choice(cat_names)

    try:
        cat = await Cat.create(
            name=cat_name,
            color=data['color'],
            image=data['image'],
            created_at=datetime.utcnow()
        )
        return cat
    except:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)


async def get_cats():
    try:
        cats = await Cat.all().order_by('-created_at')
    except DoesNotExist:
        return {"message": "No cats found."}

    return cats


async def get_cat(cat_id):
    try:
        cat = await Cat.get(id__iexact=cat_id)
    except DoesNotExist:
        return {"message": "No cat found."}
    
    return cat


async def delete_cat(cat_id):
    try:
        cat = await Cat.get(id__iexact=cat_id)
        if cat:
            await cat.delete()
            return {"message": "Cat deleted successfully"}
    except DoesNotExist:
        return {"message": "No cat found to delete."}
    

async def update_cat(cat_id, data: dict):
    try:
        cat = await Cat.get(id__iexact=cat_id)
        if cat:
            if "name" in data:
                cat.name = data.get('name')
            if "color" in data:
                cat.color = data.get('color')
            if "image" in data:
                cat.image = data.get('image')
            
            await cat.save()

        return cat
    except DoesNotExist:
        return {"message": "No cat found to update."}
