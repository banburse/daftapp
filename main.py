
# main.py

from fastapi import FastAPI


i = -1
names = []
surnames = []


app = FastAPI()



@app.get("/")
def root():
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

@app.post("/patient")
def create_patient(name, surname):
    i+=1
    names.append(name)
    surnames.append(surname)
    return {"id": i, "patient": {"name": f"{names(i)}", "surename": f"{surname(i)}"}}

@app.get("/patient/{id}")
def patient(id):
    return {"name": f"{names(i)}", "surename": f"{surname(i)}"}


