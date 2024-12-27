"""
@Time: 2024/12/27 15:41
@Author: szkingdom-11
@File: 05-自定义返回相应类型
@Project: FastAPIProject
@Software: PyCharm.
"""
from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse


app = FastAPI()


@app.get('/', response_class=HTMLResponse)
def index():
    return {'name': '张三', 'age': 20}


@app.get('/html', response_class=HTMLResponse)
def html():
    return '''
    <html>
        <head>
            <title>Hello FastAPI</title>
        </head>
        <body>
            <h1>Hello FastAPI</h1>
        </body>
    </html>
    '''







if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)