from pydantic import BaseModel
from typing import Optional

# declaring ORM Model
class Blog_Model(BaseModel):
    title: str
    body: str
    published: Optional[bool]