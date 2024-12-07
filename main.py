"""Веб-приложение для работы с пользователями и постами"""
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import SessionLocal, User, Post

app = FastAPI()

def get_db():
    """Зависимость для получения сессии базы данных"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    """Получение всех пользователей"""
    return db.query(User).all()

@app.post("/users")
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    """Создание нового пользователя"""
    user_exists = db.query(User).filter(User.email == email).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(username=username, email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    """Получение всех постов"""
    return db.query(Post).all()

@app.post("/posts")
def create_post(title: str, content: str, user_id: int, db: Session = Depends(get_db)):
    """Создание нового поста"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    new_post = Post(title=title, content=content, user_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
