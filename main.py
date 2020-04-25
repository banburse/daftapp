
# main.py
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel





app = FastAPI()


class PatientRq(BaseModel):
    name: str
    surename: str


@app.get("/hello")
def root():
    return {'message': 'hello'}
