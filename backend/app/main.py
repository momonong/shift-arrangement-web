from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from pydantic import BaseModel
from typing import Any, Annotated
from PIL import Image
from io import BytesIO
import pandas as pd

app = FastAPI()

# 允許所有源的跨域請求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello World"}

class Access_type(str, Enum):
    boss = 'boss'
    manager = 'manager'
    staff = 'staff'

@app.get('/access/{access}')
def get_access(access: Access_type):
    if access is Access_type.boss:
        return {'access': access, 'message': f'Hello, {access}!'}
    if access.value == 'manager':
        return {'access': access, 'message': f'Hello, {access}!'}
    return {'access': access, 'message': f'Hello, {access}!'}

class Item(BaseModel):
    name: str
    description:str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

@app.post('/item/', response_model=Item)
def create_item(item: Item) -> Any:
    return item

@app.get('/item/', response_model=list[Item])
def read_item() -> Any:
    return [
        {'name': 'portal gun', 'price': 50.5},
        {'name': 'plog', 'price': 30.5},
    ]

class OperatorEnum(str, Enum):
    add = 'add'
    sub = 'sub'
    mul = 'mul'
    div = 'div'

class CalculateRequest(BaseModel):
    operator: OperatorEnum
    a: int
    b: int

class CalculateResponse(BaseModel):
    result: int

@app.post('/math_post', response_model=CalculateResponse)
def calculate_post(request: CalculateRequest):
    operator = request.operator
    a = request.a
    b = request.b
    match operator:
        case OperatorEnum.add:
            return {'result': a+b}
        case OperatorEnum.sub:
            return {'result': a-b}
        case OperatorEnum.mul:
            return {'result': a*b}
        case OperatorEnum.div:
            return {'result': a/b}
        case _:
            raise HTTPException(status_code=400, detail='Invalid operator')
        
@app.get('/math_get', response_model=CalculateResponse)
def calculate_get(operator: OperatorEnum, a: int, b: int):
    operator = operator
    a = a
    b = b
    match operator:
        case OperatorEnum.add:
            return {'result': a+b}
        case OperatorEnum.sub:
            return {'result': a-b}
        case OperatorEnum.mul:
            return {'result': a*b}
        case OperatorEnum.div:
            return {'result': a/b}
        case _:
            raise HTTPException(status_code=400, detail='Invalid operator')

class GoogleForm(BaseModel):
    first_name: str
    last_name: str
    tel: str

class SudentPersonnel(str, Enum):
    boss = 'boss'
    manager = 'manager'
    staff = 'staff'  

class GoogleFormResponse(BaseModel):
    name: str
    tel: str
    personnel: str

@app.post('/google-form', response_model=GoogleFormResponse)
def google_form(google_form: GoogleForm, personnel: SudentPersonnel):
    name = f'{google_form.first_name} {google_form.last_name}'
    return {
        'name': name,
        'tel': google_form.tel,
        'personnel': personnel
    }

def CycleGAN(image: Image):
    image = image.convert('RGB')
    image = image.convert('L')
    return image

@app.post('/ai-art-portrait')
def ai_art_portrait(file: Annotated[bytes, File()]):
    image = Image.open(BytesIO(file))
    image = CycleGAN(image)
    buffer = BytesIO()
    image.save(buffer, 'jpeg')
    buffer.seek(0)
    return StreamingResponse(buffer, media_type='image/jpeg')

class BardRequest(BaseModel):
    message: str

def Bard(message: str):
    message = f'THIS IS A TEST:  {message}'
    return message 

@app.post('/bard')
def bard_endpoint(request: BardRequest):
    message = request.message
    message = Bard(message)
    return {'message': message}

class ShiftRequest(BaseModel):
    file: UploadFile

# @app.post('/shift')
# # def shift_endpoint(file: Annotated[bytes, File()]):
# #     df = pd.read_csv(BytesIO(file))
# #     name = df['112'][2]
# #     return {'message': f'csv file succesfully uploaded, {name}'}
# async def shift_endpoint(file: Annotated[UploadFile, File()]):
#     # 讀取檔案內容
#     contents = await file.read()

#     # 檢查檔案擴展名
#     if file.filename.endswith('.xlsx'):
#         df = pd.read_excel(BytesIO(contents))
#     elif file.filename.endswith('.csv'):
#         df = pd.read_csv(BytesIO(contents))
#     else:
#         return {'message': 'Unsupported file format'}

#     # 假設您要從特定列和行讀取數據
#     name = df['112'][2]
#     return {'message': f'File successfully uploaded, {name}'}

@app.post('/shift')
async def shift_endpoint(file: Annotated[UploadFile, File()]):
    contents = await file.read()

    if file.filename.endswith('.xlsx'):
        df = pd.read_excel(BytesIO(contents))
    elif file.filename.endswith('.csv'):
        df = pd.read_csv(BytesIO(contents))
    else:
        return {'message': 'Unsupported file format'}

    # 打印列名稱以進行調試
    print(df.columns)

    # 根據檔案類型選擇列名稱
    column_name = '112' if '112' in df.columns else df.columns[0]  # 假設 '112' 或第一列

    # 讀取數據
    name = df[column_name][2]
    return {'message': f'File successfully uploaded, {name}'}
