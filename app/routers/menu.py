from fastapi import Response,status,HTTPException, Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.inspection import inspect
from typing import List
from .. import models, schemas ,oauth2
from ..database import get_db



router = APIRouter(
    prefix="/getmenuassignedrole",
    tags=['Menu']
)

def instance_to_dict(instance) -> dict:
    return {c.key: getattr(instance, c.key) for c in inspect(instance).mapper.column_attrs}

# @router.get("/{id}", response_model=list[schemas.GetMenuAssignedRoleOut])
@router.get("/",response_model=List[schemas.MenuAssignedRoleOut])
def getmenuassignedrole(db: Session = Depends(get_db),
             current_user: int = Depends(oauth2.get_current_user),):
    
    response = db.query(models.UspPermission).all()

    
    if not response:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, 
                            detail=f"User with idoes not exist" )
    
    # response_json = jsonable_encoder( response )
    # print(response_json)
    return  response