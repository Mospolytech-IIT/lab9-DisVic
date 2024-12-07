from models import SessionLocal, User, Post

def fetch_all_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        for user in users:
            print(f"User: {user.username}, Email: {user.email}")
    finally:
        db.close()

def fetch_posts_with_users():
    db = SessionLocal()
    try:
        posts = db.query(Post).all()
        for post in posts:
            print(f"Post: {post.title}, Author: {post.user.username}")
    finally:
        db.close()
