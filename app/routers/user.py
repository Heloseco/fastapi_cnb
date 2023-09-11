from fastapi import FastAPI, Response,status,HTTPException, Depends, APIRouter
from .. import models, schemas ,utils,oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/users",
    tags=['Users']
)
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate,db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    hash_password = utils.hash(user.password)
    user.password = hash_password
    user.created_by = current_user.fullname
    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}",response_model= schemas.UserOut)
def get_user(id: int ,db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):

    user = db.query(models.User).filter(models.User.user_id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, 
                            detail=f"does not exist")
    return user

