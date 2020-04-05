
# main.py

from fastapi import FastAPI


i = -1
names = []
surnames = []


app = FastAPI()



@app.get("/")
def root():
    return {"message": "Zuzia to lamus"}
    ##return {"message": "Hello World during the coronavirus pandemic!"}


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
    return {"id": i, "patient": {"name": f"{names(i-1)}", "surename": f"{surname(i-1)}"}}

@app.get("/patient/{id}")
def patient(id):
    names.append(name)
    surnames.append(surname)
    return {"name": f"{names(i-1)}", "surename": f"{surname(i-1)}"}


