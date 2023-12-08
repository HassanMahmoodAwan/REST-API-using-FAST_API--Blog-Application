from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from __init__ import schema, database, models

router = APIRouter()

get_db = database.get_db




# ---  GET all the Blogs ----
@router.get('/blog', tags=['Blog'])
def all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# --- Post Method ---
@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['Blog'])
def blog(request: schema.Blog_Model, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# ---- Single Particular Blog ----
@router.get('/blog/{id}', status_code = 200, tags=['Blog'])
def show_blog(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=404, 
        detail=f'blog with id {id} not found 404')   # Best way
        # response.status_code = 404
        # return {'detail': f'blog with id {id} not found 404'}

    return blog


# --- Delete particular Blog ---
@router.delete('/blog/{id}', status_code = 204, tags=['Blog'])
def delete_blog(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=404, detail='Blog not found')
    
    blog.delete(synchronize_session = False)
    db.commit()
    return 'Deletion done'


# --- UPDATE ---
@router.put('/blog/{id}', status_code = 202, tags=['Blog'])
def update_blog(id, response: Response, request:schema.Blog_Model, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)

    if not blogs.first():
        raise HTTPException(status_code=404, 
        detail=f'blog with id {id} not found 404')
        return

    blogs.update({"title": request.title, "body": request.body}, synchronize_session=False)
    db.commit()
    return 'Blog Updated Successfully'