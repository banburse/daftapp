
# main.py
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates




app = FastAPI()
templates = Jinja2Templates(directory="templates")

class PatientRq(BaseModel):
    name: str
    surename: str


@app.get("/hello")
def root():
    return {'message': 'hello'}
