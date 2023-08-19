from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class UserOut(BaseModel):
    user_id: int
    fullname: str
    email: EmailStr
    branch_id: int
    roleid: int
    created_by: str
    created_date: datetime
    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    create_date: datetime
    owner_id: int
    owner: UserOut
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

# User 
class UserCreate(BaseModel):
    fullname: str
    email: EmailStr
    password: str
    branch_id: int
    roleid: int
    created_by: Optional[str] = None



class UserLogin(BaseModel):
    email: EmailStr
    password: str



class Token (BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

# Menu
class MenuAssignedRoleOut(BaseModel):
    pmsid: int
    pms_menu_name: str
    pms_menu_level: int
    pms_parent_id: Optional[int]
    pms_page_name: str
    pms_menu_type: str
    pms_menu_index: int
    pms_menu_image: str
    created_date: datetime
    created_by: str
    modified_date:Optional[datetime]
    modified_by: Optional[str]
    db_id: Optional[int]
    to_name: str
    pms_parent_name: Optional[int] = None

