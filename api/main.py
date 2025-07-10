from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, SessionLocal
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/posts/", response_model=schemas.TesteSistemaOut)
def create_post(post: schemas.TesteSistemaCreate, db: Session = Depends(get_db)):
    return crud.create_test(db, post)

@app.get("/posts/", response_model=list[schemas.TesteSistemaOut])
def list_posts(db: Session = Depends(get_db)):
    return crud.get_all_tests(db)

@app.get("/posts/{post_id}", response_model=schemas.TesteSistemaOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_test_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.put("/posts/{post_id}", response_model=schemas.TesteSistemaOut)
def update_post(post_id: int, updated_post: schemas.TesteSistemaUpdate, db: Session = Depends(get_db)):
    post = crud.update_test(db, post_id, updated_post)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.delete_test(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
