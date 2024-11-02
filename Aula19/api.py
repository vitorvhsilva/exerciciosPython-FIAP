from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

class Request(BaseModel):
    num1: float
    num2: float
    oper: str

@app.get("/")
async def teste():
    return "oi"

@app.post('/', response_class=HTMLResponse)
async def calcular(request: Request):

    num1 = int(request.num1)
    num2 = int(request.num2)
    oper = str(request.oper)

    resultado = 0

    if oper == 'soma':
        resultado = soma(num1, num2)
    if oper == 'sub':
        resultado = sub(num1, num2)
    if oper == 'mult':
        resultado = mult(num1, num2)
    if oper == 'div':
        resultado = div(num1, num2)

    return str(resultado)

def soma(num1:int, num2: int):
    return num1 + num2

def sub(num1:int, num2: int):
    return num1 - num2

def mult(num1:int, num2: int):
    return num1 * num2

def div(num1:int, num2: int):
    return num1 / num2

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.2", port=8000)