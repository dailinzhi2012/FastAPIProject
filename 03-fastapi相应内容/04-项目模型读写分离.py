"""
@Time: 2024/12/27 14:11
@Author: szkingdom-11
@File: 03-复杂嵌套的响应模型
@Project: FastAPIProject
@Software: PyCharm.
"""
from typing import List
from fastapi import FastAPI, Path
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class UserBase(BaseModel):
    username: str


class LoginForm(UserBase):
    password: str


class RegisterForm(LoginForm):
    password_confirm: str


class ReadUser(UserBase):
    email: str
    age: int
    mobile: str
    address: str
    sex: str
    is_active: bool
    is_superuser: bool


@app.post('/user/register', status_code=201)
def register(item: RegisterForm):
    return item.model_dump()


@app.post('/user/login', status_code=200)
def login(item: LoginForm):
    return item.model_dump()





if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
