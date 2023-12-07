from pydantic import BaseModel
from typing import Optional

# declaring ORM Model
class Blog_Model(BaseModel):
    title: str
    body: str
    published: Optional[bool]


# Showing this model
class ShowBlog(Blog_Model):
    class Config():
        orm_mode = True
    


# ==== User Registeration Schema Pydantic =====
class user(BaseModel):
    name: str
    email: str
    password: str