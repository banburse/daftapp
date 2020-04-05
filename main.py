
# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Zuzia to lamus"}
    ##return {"message": "Hello World during the coronavirus pandemic!"}


@app.get("/method")
def root(method):
    return {"method": "GET"}

@app.post("/method")
def root(method):
    return {"method": "POST"}

@app.put("/method")
def root(method):
    return {"method": "PUT"}

@app.delete("/method")
def root(method):
    return {"method": "DELETE"}




