from fastapi import FastAPI, File, UploadFile
from parsingService import parse_tab
import uuid
import os
import shutil

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/parsetabtest")
def parse_tab_post():
    return parse_tab("The Witcher - Toss a Coin to Your Witcher.gp5")

@app.post("/parsetab")
async def parsetab(file: UploadFile = File(...)):
    localFilename = str(uuid.uuid4()) + '.' + file.filename.split('.')[-1]

    with open(localFilename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    parsedData = parse_tab(localFilename)

    os.remove(localFilename)

    return parsedData