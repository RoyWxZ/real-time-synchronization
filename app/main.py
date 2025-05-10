from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    price: float

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Stempro!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created", "item": item}