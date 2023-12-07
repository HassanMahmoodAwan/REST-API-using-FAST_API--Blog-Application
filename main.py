# TO run Server, Command: uvicorn main:app --reload

from fastapi import FastAPI, Depends, Response, status, HTTPException
import uvicorn
from sqlalchemy.orm import Session
from __init__ import models, database, schema


app = FastAPI()

models.Base.metadata.create_all(bind = database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get('/')
def home():
    return {'Home': 'Page will have home content'}


# ====== Blog PAGE ======== #
# --- Post Method ---
@app.post('/blog', status_code=status.HTTP_201_CREATED)
def blog(request: schema.Blog_Model, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# ---  GET all the Blogs ----
@app.get('/blog')
def all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# ---- Single Particular Blog ----
@app.get('/blog/{id}', status_code = 200)
def show_blog(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=404, 
        detail=f'blog with id {id} not found 404')   # Best way
        # response.status_code = 404
        # return {'detail': f'blog with id {id} not found 404'}

    return blog

# --- Delete particular Blog ---
@app.delete('/blog/{id}', status_code = 204)
def delete_blog(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=404, detail='Blog not found')
    
    blog.delete(synchronize_session = False)
    db.commit()
    return 'Deletion done'
    

# --- UPDATE ---
@app.put('/blog/{id}', status_code = 202)
def update_blog(id, response: Response, request:schema.Blog_Model, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)

    if not blogs.first():
        raise HTTPException(status_code=404, 
        detail=f'blog with id {id} not found 404')
        return

    blogs.update({"title": request.title, "body": request.body}, synchronize_session=False)
    db.commit()
    return 'Blog Updated Successfully'






if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)