"""Скрипт для извлечения данных из базы данных"""
from sqlalchemy.orm import Session
from models import SessionLocal, User, Post

def fetch_all_users() -> None:
    """Выводит всех пользователей"""
    db: Session = SessionLocal()
    try:
        users = db.query(User).all()
        for user in users:
            print(f"User: {user.username}, Email: {user.email}")
    finally:
        db.close()

def fetch_posts_with_users() -> None:
    """Выводит все посты вместе с пользователями"""
    db: Session = SessionLocal()
    try:
        posts = db.query(Post).all()
        for post in posts:
            print(f"Post: {post.title}, Author: {post.user.username}")
    finally:
        db.close()

if __name__ == "__main__":
    fetch_all_users()
    fetch_posts_with_users()
