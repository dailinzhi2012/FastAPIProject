"""
File Name: 04-请求体参数之表单参数
Author: Nagasawa
Date: 2024/12/26
"""

from fastapi import FastAPI,Form
import uvicorn
from typing import Union

app = FastAPI()

@app.post("/api/users/login/")
def login(username:str=Form(description="用户名",min_length=5,max_length=10),
          password:str=Form(description="密码",min_length=8,max_length=16)
          ):
    return {"username":username,"password":password}

if __name__ == '__main__':
    uvicorn.run(app='04-请求体参数之表单参数:app', host='127.0.0.1', port=8000, reload=True)