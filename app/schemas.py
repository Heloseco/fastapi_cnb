from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional,Dict
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
    roleid: Optional[int]
    phone_number: Optional[int]
    created_by: str
    created_date: datetime
    modified_by: Optional[str]
    modified_date: Optional[datetime]
    last_pwd_modified_date:Optional[datetime]
    description: Optional[str]
    deviceid: Optional[str]
    
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
    user: UserOut
    access_token: Dict[str, str]
    # token_type: str

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    id: Optional[str] = None
class MenuBase(BaseModel):
    # pmsid: Optional[int]
    pms_menu_name: str
    pms_menu_level: int
    pms_parent_id: Optional[int]
    to_name: str
    pms_menu_type: str
    pms_menu_index: int
    pms_menu_image: str
    created_date: Optional[datetime]
    created_by: Optional[str]
    modified_date:Optional[datetime]
    modified_by: Optional[str]
    db_id: Optional[int]
class MenuCreate(MenuBase):
    pass

class Menu(MenuBase):
    pass
# Menu
class MenuAssignedRoleOut(BaseModel):
    pmsid: Optional[int]
    pms_menu_name: str
    pms_menu_level: int
    pms_parent_id: Optional[int]
    to_name: str
    pms_menu_type: str
    pms_menu_index: int
    pms_menu_image: str
    created_date: datetime
    created_by: str
    modified_date:Optional[datetime]
    modified_by: Optional[str]
    db_id: Optional[int]
    # pms_parent_name: int = "1"


