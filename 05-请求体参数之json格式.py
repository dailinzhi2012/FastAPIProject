"""
File Name: 04-请求体参数之表单参数
Author: Nagasawa
Date: 2024/12/26
"""

from fastapi import FastAPI, Form
import uvicorn
from pydantic import BaseModel, Field

app = FastAPI()


@app.post("/api/users/login/")
def login(username: str = Form(description="用户名", min_length=5, max_length=10),
          password: str = Form(description="密码", min_length=8, max_length=16)
          ):
    return {"username": username, "password": password}


# ===============json格式的参数定义=================
"""
1. 使用pydantic的BaseModel定义json格式的参数
2. 在视图处理函数中指定参数的乐行为BaseModel定义的模型
"""


class RegisterInfo(BaseModel):
    username: str
    password: str
    password_confirm: str
    email: str

@app.post("/api/users/register/")
def register(item: RegisterInfo):
    return item.dict()


# ===================参数嵌套格式========================
class Mobile(BaseModel):
    mobile: str = Field(
        ...,
        description="手机号",
        min_length=11,
        max_length=11,
        pattern=r'\d{11}'

    )
    code: str

class Address(BaseModel):
    street: str
    city: str
    province: str
    mobile: list[Mobile]

class UserInfo(BaseModel):
    username: str
    email: str
    address: Address

@app.post("/api/users/info/")
def user_info(item: UserInfo):
    return item.model_dump()


if __name__ == '__main__':
    uvicorn.run(app='05-请求体参数之json格式:app', host='127.0.0.1', port=8000, reload=True)
