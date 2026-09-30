from fastapi import FastAPI , Request
from pydantic import BaseModel

app = FastAPI()


dict1 = {
    "1" : "satish ",
    "2" : "kumar"   
}
@app.get("/")
def read_root():
    return {"Hello": "Nothing"}

@app.get("/getlist")
def read_root():
    return dict1

@app.get("/message")
def read_root():
    return {"Hello": "World"}

@app.get("/Satish")
def read_root():
    return {"Hello": "Satish"}  

# @app.post("/postlist")
# def read_root(request : Request):
#     print(request)
#     return dict1
class Item(BaseModel):
    name: str
@app.post("/postlist")
def post_list(item: Item):
    new_id = str(len(dict1) + 1)
    dict1[new_id] = item.name
    return dict1

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}