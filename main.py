from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from pydantic.types import NonNegativeFloat

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

app = FastAPI()

@app.post("/item/")
async def create_item(item: Item):
    return {"message": f"{item.name}は、税込価格{int(item.price*item.tax)}円です。"}

# @app.get("/")
# async def index():
#     return {"message": "Hello Work"}

# パス&クエリパラメータ

# @app.get("/countries/{country_name}")
# async def country(country_name: str = 'japan', city_name: str ='tokyo'):
#     return {
#         "country_name": country_name,
#         "city_name": city_name
#     }