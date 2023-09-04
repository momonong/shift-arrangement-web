from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
import datetime

class Access_type(str, Enum):
    boss = 'boss'
    manager = 'manager'
    staff = 'staff'

class Cal(int, Enum):
    a: int
    b: int

class Delivery(BaseModel):
    timestamp: datetime
    dimensions: tuple[int, int]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/access/{access}')
async def get_access(access: Access_type):
    if access is Access_type.boss:
        return {'access': access, 'message': f'Hello, {access}!'}
    if access.value == 'manager':
        return {'access': access, 'message': f'Hello, {access}!'}
    return {'access': access, 'message': f'Hello, {access}!'}

@app.post('/math')
async def calculate(calculation: Cal):
    operator, a, b = request.operator, request.a, requset.b
    match operator:
        case 