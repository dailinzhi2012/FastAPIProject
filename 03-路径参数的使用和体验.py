"""
File Name: 03-路径参数的使用和体验
Author: Nagasawa
Date: 2024/12/26
"""

from fastapi import FastAPI,Path
import uvicorn
from typing import Union

app = FastAPI()


# 路径参数的定义:在路径中使用{}包裹起来的参数就是路径参数
@app.get("/project/{project_id}")
def get_project(project_id: int, name: str):
    return {"project_id": project_id, "name": name}

# 路径参数校验：
@app.get("/env/{env_id}")
def get_project2(env_id: Union[int, None] = Path(
    description="环境ID",
    gt=0,
    title="环境ID",
    le=100,
)):
    return {"env": env_id}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
