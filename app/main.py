from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models 
from .database import engine
from .routers import post, user,auth , vote, menu
from .config import Setting


#  auto generate table to DB
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    # # How to Disable the Docs (Swagger UI and ReDoc)
    # docs_url=None, # Disable docs (Swagger UI)
    # redoc_url=None, # Disable redoc
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
app.include_router(menu.router)


@app.get("/")
def read_root():
    return {"message": "wecome to my api"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)