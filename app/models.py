from .database import Base
from sqlalchemy import Column, Integer,String, Boolean, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.dialects.postgresql import JSONB

class Company(Base):
    __tablename__ = 'companys'

    company_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String, nullable=False, unique=True)
    company_code = Column(String, nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default= text('now()'))
    created_by = Column(String, nullable=False)
    modified_date = Column(TIMESTAMP(timezone=True))
    modified_by = Column(String)

class UspBranch(Base):
    __tablename__ = 'usp_branchs'

    branch_id = Column(Integer, primary_key=True, autoincrement=True)
    branch_code = Column(String, nullable=False)
    branch_name = Column(String, nullable=False, unique=True)
    opening_date = Column(Date)
    range_ip = Column(Integer, nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default= text('now()'))
    created_by = Column(String, nullable=False)
    modified_date = Column(TIMESTAMP(timezone=True))
    modified_by = Column(String)
    tvticketip = Column(JSONB)

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer,primary_key=True, nullable= False, autoincrement=True)
    fullname = Column(String, nullable=False)
    email = Column(String , nullable=False ,unique=True)
    password = Column(String, nullable=False)
    last_pwd_modified_date = Column(TIMESTAMP(timezone=True))
    phone_number = Column(String)
    branch_id = Column(Integer, ForeignKey("usp_branchs.branch_id",ondelete="CASCADE",onupdate="CASCADE"),nullable=False,)
    status = Column(Integer)
    roleid = Column(Integer, nullable=False)
    counterno = Column(String)
    created_date = Column(TIMESTAMP(timezone=True),nullable=False, server_default= text('now()'))
    created_by = Column(String, nullable=False)
    modified_date = Column(TIMESTAMP(timezone=True))
    modified_by = Column(String)
    description = Column(String)
    deviceid = Column(Text)
    branch = relationship("UspBranch")

class UspPermission(Base):
    __tablename__ = 'menu_permission'

    pmsid = Column(Integer, primary_key=True, nullable=False)
    pms_menu_name = Column(String, nullable=False)
    pms_menu_level = Column(Integer, nullable=False)
    pms_parent_id = Column(Integer)
    pms_page_name = Column(String, nullable=False, unique=True)
    pms_menu_type = Column(Integer)
    pms_menu_index = Column(Integer)
    pms_menu_image = Column(String)
    created_date = Column(TIMESTAMP(timezone=True),nullable=False, server_default= text('now()'))
    created_by = Column(String)
    modified_date = Column(TIMESTAMP(timezone=True))
    modified_by = Column(String)
    db_id = Column(Integer)
    to_name = Column(String)



class Vote(Base):
    __tablename__ = "votes"
    post_id = Column(Integer, ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id",ondelete="CASCADE"),primary_key=True)



class Post(Base):
    __tablename__= "posts"

    id = Column(Integer,primary_key=True, nullable= False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default= 'True', nullable=False)
    create_date = Column(TIMESTAMP(timezone=True),nullable=False, server_default= text('now()'))
    owner_id  = Column(Integer, ForeignKey("users.user_id",ondelete="CASCADE"),nullable=False)
    owner = relationship("User")



