
# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World during the coronavirus pandemic!"}

@app.get("/GET")
def root(method):
    return {"method": 'GET'}

@app.post("/POST")
def root(method):
    return {"method": 'POST'}

@app.put("/PUT")
def root(method):
    return {"method": 'PUT'}

@app.delete("/DELETE")
def root(method):
    return {"method": "DELETE"}

