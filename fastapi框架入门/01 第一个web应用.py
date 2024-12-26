"""
 ---encoding:utf-8---
@Time : 2024/12/26 16:39
@Author : szkingdom-11
@File : 01 第一个web应用
@Project : FastAPIProject
@Software: PyCharm.
"""
from fastapi import FastAPI
import uvicorn

# 创建一个FastAPI应用
app = FastAPI()

# 开发第一个接口
@app.get("/")
async def root():
    return {"message": "Hello World", "code": 1001, "data": []}

@app.post("/api/user/login/", summary="用户登录")
async def login(username: str, password:str):
    return {"message":"登陆成功","code":1000,"data":{
        "username": username,
        "password": password,
    }}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)