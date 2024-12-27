"""
@Time: 2024/12/27 09:57
@Author: szkingdom-11
@File: 01自定义响应状态码
@Project: FastAPIProject
@Software: PyCharm.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

cases = [
    {
        "id": 1,
        "name": "张三",
        "age": 20,
        "gender": "男",
        "address": "北京市海淀区"
    },
    {
        "id": 2,
        "name": "李四",
        "age": 25,
        "gender": "女",
        "address": "上海市浦东新区"
    }
]


class CaseModel(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    address: str | None = None


@app.get("/cases", status_code=200)
def get_all_cases():
    """
    获取所有案例信息
    :return:
    """
    return cases


@app.post("/cases", status_code=201)
def create_case(case: CaseModel):
    """
    创建一个用例
    :param case:
    :return:
    """
    cases.append(case.model_dump())
    return case


@app.put("/cases/{case_id}/", status_code=200)
def update_case_id(case_id: int, case: CaseModel):
    """
    更新一个用例
    :param case_id:
    :param case:
    :return:
    """
    # 先找到要更新的用例
    for i, c in enumerate(cases):
        if c['id'] == case_id:
            cases[i] = case.model_dump()
            return case


@app.delete('/cases/{case_id}', status_code=204)
def delete_case(case_id: int):
    """
    删除一个用例
    :param case_id:
    :return:
    """
    # 先找到要删除的用例
    for i, c in enumerate(cases):
        if c['id'] == case_id:
            del cases[i]
            return


"""
restful Api设计规范：
新增数据：状态码201
删除数据：状态码204
修改数据：状态码200
查询数据：状态码200
"""

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
