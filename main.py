from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBasic, HTTPBasicCredentials


fake_database = {"trudnY": "PaC13Nt"}

class LoginModel(BaseModel):
    username: str
    password: str


app = FastAPI()
security = HTTPBasic()
templates = Jinja2Templates(directory="templates")



@app.get("/users/me")
def read_user(credentials: HTTPBasicCredentials= Depends(security)):
    return {"username": credentials.username, "password": credentials.password}

@app.get("/login")
def getlogin():
    return templates.TemplateResponse("loginpage.html")

@app.post("/login")
def postlogin(user: LoginModel):
    if user.username == "trudnY" and user.password == "PaC13Nt":
        return True
    else:
        raise HTTPException(status_code=401, detail="No content")
