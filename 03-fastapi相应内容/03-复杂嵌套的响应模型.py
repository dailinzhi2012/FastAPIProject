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


class Item(BaseModel):
    id: int
    name: str
    price: float


class Order(BaseModel):
    order_id: int
    status: str = "未支付"
    items: List[Item]


@app.get('/items', response_model=List[Item])
def get_all_items():
    return [
        {"id": 1, "name": "apple", "price": 18.8},
        {"id": 2, "name": "banana", "price": 21.8},
    ]


@app.get('/order/{id}', response_model=Order)
def get_order(id: int = Path(..., gt=0, lt=100)):
    return {
        "order_id": id,
        "status": "已支付",
        "items": [
            {"id": 1, "name": "apple", "price": 18.8},
            {"id": 2, "name": "banana", "price": 21.8},
        ]}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
