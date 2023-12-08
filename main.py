# TO run Server, Command: uvicorn main:app --reload

from fastapi import FastAPI
from sqlalchemy.orm import Session
from __init__ import models, database
from routers import blog, user
import uvicorn

app = FastAPI()

models.Base.metadata.create_all(bind = database.engine)

app.include_router(blog.router)
app.include_router(user.router)




# ==== Home Page route Developed ====
@app.get('/')
def home():
    return {'Home': 'Page will have home content'}





if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)