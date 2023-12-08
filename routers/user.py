from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from __init__ import schema, database, models, hashing

router = APIRouter()

get_db = database.get_db



# ====== User Registeration =======
@router.post('/user', status_code=status.HTTP_201_CREATED, tags=['User'])
def user_registeration(request: schema.user, db: Session = Depends(get_db)):
    new_user = models.User(name = request.name, email = request.email, password=hashing.Hash.pwd_bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return 'New user Added'


@router.get('/user', status_code = 200, tags=['User'])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users