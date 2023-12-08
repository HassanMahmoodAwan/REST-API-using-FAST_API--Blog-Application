from fastapi import APIRouter, Depends, status, HTTPException
from __init__ import schema, models, database, hashing, JWToken
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix = '/login',
    tags = ['Authentication']
)


get_db = database.get_db


@router.post('/', status_code = 201)
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()

    if not user:
        raise HTTPException(status_code=404, 
        detail='Invalid Credientials')

    if not hashing.Hash.verify(request.password, user.password):
        raise HTTPException(status_code=404, 
        detail='Wrong Password')

    
    access_token = JWToken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

