from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


class Shots(BaseModel):
    number: int
    name: str
    squence: str
    department: Optional[str] = None

shots = {
    1001: {"number": 1001,
        "name": "shot01",
        "sequence": "some seq",
        "department": "FX"},
    1002: {"number": 1002,
        "name": "shot02",
        "sequence": "some other seq",
        "department": "Animation"}
}

@app.get("/")
def index():
    return shots

@app.get("/get-shot/{shot_num}")
def get_shot_by_number(shot_num: int = Path(description="Input the shot number for the shot in the sequence")):
    return shots[shot_num]

@app.get("/get-shot-by-name/{shot_name}")
def get_shot_by_name(shot_name):
    for shot in shots:
        if shots[shot]["name"] == shot_name:
            return shots[shot]
        