from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>Welcome to the Employee Events Dashboard!</h1>"

@app.get("/employees", response_class=HTMLResponse)
def employees():
    return "<h2>Employee List</h2>"
