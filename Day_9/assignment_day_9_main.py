# fastapi
# Question-18:
# convert helloj of flask to fastapi
   
from fastapi import FastAPI , Request
from pydantic import BaseModel

app = FastAPI()

class Hello_Item(BaseModel):
    name:str
    format:str="Json"
    
@app.get("/helloj/{name}/{format}")
@app.get("/helloj")
async def get_hello(name: str=None, format: str="Json"):
    return {"name": name, "format": format}


@app.post("/helloj")
async def post_hello(hello_item: Hello_Item):
    return {"name": hello_item.name, "format": hello_item.format}
