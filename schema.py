from pydantic import BaseModel
from typing import Optional

# declaring ORM Model
class Blog_Model(BaseModel):
    title: str
    body: str
    published: Optional[bool]


# Showing this model            # Not working
class ShowBlog(Blog_Model):
    class Config():
        orm_mode = True
    


# ==== User Registeration Schema Pydantic =====
class user(BaseModel):
    name: str
    email: str
    password: str



# ==== Login system =====
class login(BaseModel):
    email: str
    password: str



# =====JWT TOKEN =======
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None