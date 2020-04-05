
# main.py

from fastapi import FastAPI




app = FastAPI()

app.counter = -1
app.counterlist = []
app.names = []
app.surnames = []

@app.get("/")
def root():
    return {"message": "Zuzia to lamus"}
    ##return {"message": "Hello World during the coronavirus pandemic!"}
    ##return {"message": "3mess"}


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
    app.counter += 1
    app.names.append(name)
    app.surnames.append(surname)
    app.counterlist.append(app.counter)
    return {"id": i, "patient": {"name": f"{names(i)}", "surename": f"{surname(i)}"}}

@app.get("/patient/{id}")
def patient(id):
    if id is in app.conterlist:
        return {"name": f"{names(i)}", "surename": f"{surname(i)}"}
    else:
        return {"fail": "fail"}


