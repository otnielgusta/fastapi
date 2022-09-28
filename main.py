from typing import Optional, Union

from fastapi import FastAPI, Header, Response, Cookie

from pydantic import BaseModel

class Item(BaseModel):
    id: int
    descricao:str
    valor: float

app = FastAPI()


@app.get("/")
def read_root(user_agent:Optional[str] = Header(None)):
    return {"user-agent": user_agent}


@app.get("/cookies")
def cookie(response: Response):
    response.set_cookie(key="meucookie", value="otniellindo")
    return {"cookie": True}

@app.get("/get-cookies")
def get_cookie(meucookie: Optional[str] = Cookie(None)):
    return {"cookie": meucookie}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/item")
def add_item(item:Item, outro_item:Item):
    return [item, outro_item]