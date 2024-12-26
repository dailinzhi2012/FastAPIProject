"""
 ---encoding:utf-8---
@Time    : 2024/12/26 16:52
@Author  : szkingdom-11
@File    : 02 请求参数的定义和校验
@Project : FastAPIProject
@Software: PyCharm
"""

import uvicorn
from fastapi import FastAPI, Query
from typing import Union

# 创建一个FastAPI应用
app = FastAPI()


# 请求参数的定义和校验

@app.get("/demo")
def demo(name: str, age: int):
    """

    :param name:  查询参数name
    :param age:     查询参数age
    :return:
    """
    return {"name": name, "age": age}


@app.get("/demo/page")
def demo_page(page: str | None = None, size: Union[int, None] = None):
    """
    给查询参数设置默认值
    下面两种都是声明默认参数，以及参数的类型
    page: str | None = None
    size: Union[int, None] = None
    """
    return {"page": page, "size": size}


#  查询参数的校验

@app.get("/demo/page/check")
def demo_page_check(token: Union[str, None] = Query(
    default=None,
    min_length=5,
    max_length=10,
    title="这个是一个token",
    description="参数的描述说明信息",
    deprecated=True,
    alias="token"
)):
    return {"token": token}


# 运行FastAPI应用
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
