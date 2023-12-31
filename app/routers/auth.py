from fastapi import APIRouter, Depends , status, HTTPException , Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm   #instead : schemas.UserLogin
from sqlalchemy.orm import Session
from .. import database, schemas, models,utils, oauth2

router = APIRouter(
    tags=['Authentication']
)

# @router.post("/login")
# def login(user_credentail: schemas.UserLogin, db: Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.email == user_credentail.email).first()

#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail=f"Invalid Credentails")
#     if not utils.verify(user_credentail.password , user.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail=f"Invalid Credentails")
    
#     # create token
#     # retuern token
#     access_token = oauth2.create_access_token(data={"user_id": user.id})
#     return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login",response_model=schemas.Token)
def login(user_credentail: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.email == user_credentail.username).first()

    if user.status == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User Inactive")
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail=f"Invalid Credentails (Username)")
    if not utils.verify(user_credentail.password , user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail=f"Invalid Credentails (Password)")
    
    access_token = oauth2.create_access_token(data={"user_id": user.user_id})
    # print(access_token)
    return {"access_token": access_token,"user": user}