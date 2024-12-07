from models import SessionLocal, User, Post

# Добавление данных в таблицы
def add_users_and_posts():
    db = SessionLocal()
    try:
        # Добавляем пользователей
        user1 = User(username="user1", email="user1@example.com", password="password1")
        user2 = User(username="user2", email="user2@example.com", password="password2")
        db.add_all([user1, user2])
        db.commit()
        
        # Добавляем посты
        post1 = Post(title="Post 1", content="Content of Post 1", user_id=user1.id)
        post2 = Post(title="Post 2", content="Content of Post 2", user_id=user2.id)
        db.add_all([post1, post2])
        db.commit()
    finally:
        db.close()

add_users_and_posts()
