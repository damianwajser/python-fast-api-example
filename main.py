from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/auto")
def read_root():
    return {"patente": "abcd1234"}
