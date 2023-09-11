from .database import Base
from sqlalchemy import Column, Integer,String, Boolean, ForeignKey, Date, Text,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.dialects.postgresql import JSONB

class Company(Base):
    __tablename__ = 'companys'

    company_id = Column(Integer, primary_key=True, autoincrement=True,nullable= False)
    company_name = Column(String, nullable=False, unique=True)
    company_code = Column(String, nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default= text('now()'))
    created_by = Column(String, nullable=False)
    modified_date = Column(TIMESTAMP(timezone=True))
    modified_by = Column(String)
    opening_date = Column(TIMESTAMP(timezone=True),server_default= text('now()'))

class UspBranch(Base):
    __tablename__ = 'usp_branchs'

    branch_id = Column(Integer, primary_key=True, autoincrement=True,nullable= False)
    branch_code = Column(String, nullable=False)
    branch_name = Column(String, nullable=False, unique=True)
    opening_date = Column(Date)
    range_ip = Column(Integer, nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default= text('now()'))
    created_by = Column(String, nullable=False)
    modified_date = Column(TIMESTAMP(timezone=True))
    modified_by = Column(String)
    tvticketip = Column(JSONB)
    company_id = Column(Integer, ForeignKey("companys.company_id",ondelete="CASCADE",onupdate="CASCADE"),nullable=False,)
     
# Model Role
class UspRole(Base):
    __tablename__ = 'usp_role'

    roleid = Column(Integer, primary_key=True,nullable=False, autoincrement=True)
    rolecode = Column(String, nullable=False, unique=True)
    rolename = Column(String, nullable=False, unique=True)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default= text('now()'))
    created_by = Column(String)
    modified_date = Column(TIMESTAMP(timezone=True))
    modified_by = Column(String)

    __table_args__ = (
        UniqueConstraint('rolecode', name='usp_role_rolecode_key'),
        UniqueConstraint('rolename', name='usp_role_rolename_key')
    )

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer,primary_key=True, nullable= False, autoincrement=True)
    fullname = Column(String, nullable=False)
    email = Column(String , nullable=False ,unique=True)
    password = Column(String, nullable=False)
    last_pwd_modified_date = Column(TIMESTAMP(timezone=True))
    phone_number = Column(String)
    branch_id = Column(Integer, ForeignKey("usp_branchs.branch_id",ondelete="CASCADE",onupdate="CASCADE"),nullable=False,)
    status = Column(Boolean, nullable=False, server_default= text('true'))
    roleid = Column(Integer, ForeignKey('usp_role.roleid'), nullable=False)
    counterno = Column(String)
    created_date = Column(TIMESTAMP(timezone=True),nullable=False, server_default= text('now()'))
    created_by = Column(String, nullable=False)
    modified_date = Column(TIMESTAMP(timezone=True))
    modified_by = Column(String)
    description = Column(String)
    deviceid = Column(Text)
    branch = relationship("UspBranch")
    role = relationship("UspRole")

class MenuPermission(Base):
    __tablename__ = 'menu_permission'

    pmsid = Column(Integer,primary_key=True, nullable= False, autoincrement=True)
    pms_menu_name = Column(String,unique=True,nullable=False)
    pms_menu_level = Column(Integer,)
    pms_parent_id = Column(Integer)
    to_name = Column(String, unique=True, nullable=False)
    pms_menu_type = Column(Integer)
    pms_menu_index = Column(Integer)
    pms_menu_image = Column(String)
    created_date = Column(TIMESTAMP(timezone=True), server_default= text('now()'))
    created_by = Column(String)
    modified_date = Column(TIMESTAMP(timezone=True))
    modified_by = Column(String)
    db_id = Column(Integer)

class UspRuleNpmsAssign(Base):
    __tablename__ = 'usp_rule_npms_assign'

    rnpa_id = Column(Integer, primary_key=True,nullable=False, autoincrement=True)
    roleid = Column(Integer, ForeignKey('usp_role.roleid'), nullable=False)
    pmsid = Column(Integer, ForeignKey('menu_permission.pmsid'))
    p_view = Column(Boolean, server_default= text('false'))
    p_view_data = Column(Boolean,nullable=False, server_default= text('false'))
    p_refresh = Column(Boolean,nullable=False, server_default= text('false'))
    p_search = Column(Boolean,nullable=False, server_default= text('false'))
    p_add = Column(Boolean,nullable=False, server_default= text('false'))
    p_edit = Column(Boolean, nullable=False,server_default= text('false'))
    p_delete = Column(Boolean, nullable=False,server_default= text('false'))
    p_save = Column(Boolean,nullable=False, server_default= text('false'))
    p_print = Column(Boolean,nullable=False, server_default= text('false'))
    p_import = Column(Boolean,nullable=False, server_default= text('false'))
    p_export = Column(Boolean, nullable=False,server_default= text('false'))
    created_date = Column(TIMESTAMP(timezone=True), server_default= text('now()'))
    created_by = Column(String)
    modified_date = Column(Date)
    modified_by = Column(String)
    role = relationship("UspRole")
    menu = relationship("MenuPermission")

# class Vote(Base):
#     __tablename__ = "votes"
#     post_id = Column(Integer, ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.user_id",ondelete="CASCADE"),primary_key=True)

# class Post(Base):
#     __tablename__= "posts"

#     id = Column(Integer,primary_key=True, nullable= False)
#     title = Column(String, nullable=False)
#     content = Column(String, nullable=False)
#     published = Column(Boolean, server_default= 'True', nullable=False)
#     create_date = Column(TIMESTAMP(timezone=True),nullable=False, server_default= text('now()'))
#     owner_id  = Column(Integer, ForeignKey("users.user_id",ondelete="CASCADE"),nullable=False)
#     owner = relationship("User")



