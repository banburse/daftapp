
# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from requests.auth import HTTPBasicAuth





app = FastAPI()

app.counter = 0

class PatientRq(BaseModel):
    name: str
    surename: str

class PatientResp(BaseModel):
    id: str
    patient: dict



@app.get("/")
def root():
    ##return {"message": "Zuzia to lamus"}
    return {"message": "Hello World during the coronavirus pandemic!"}
    ##return {"message": "3mess"}
    
@app.get("/welcome")
def some_method():
    ##return {"message": "Zuzia to lamus"}
    ##return {"message": "Hello World during the coronavirus pandemic!"}
    return {"message": "3mess"}





@app.get("/method")
def metoda():
    return{"method": "GET"}

@app.post("/method")
def metoda():
    return{"method": "POST"}

@app.put("/method")
def metoda():
    return{"method": "PUT"}

@app.delete("/method")
def metoda():
    return{"method": "DELETE"}

@app.get('/num/{p}')
def counter(p):
    return str(p)

@app.post("/patient")
def create_patient(rq: PatientRq):
    app.counter += 1
    return PatientResp(id=str(app.counter), patient=rq.dict())

@app.get("/patient/{pk}")
def patient_finder(pk):
    if int(pk) > app.counter:
        raise HTTPException(status_code=204, detail="No content")
    return PatientRq(name="NAME", surename="SURENAME")


