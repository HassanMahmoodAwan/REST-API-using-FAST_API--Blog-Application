from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from __init__ import schema, database, models, hashing

router = APIRouter(
    prefix = '/user',
    tags = ['Users']
)

get_db = database.get_db



# ====== User Registeration =======
@router.post('/', status_code=status.HTTP_201_CREATED)
def user_registeration(request: schema.user, db: Session = Depends(get_db)):
    new_user = models.User(name = request.name, email = request.email, password = hashing.Hash.pwd_bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return 'New user Added'


@router.get('/', status_code = 200)
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users