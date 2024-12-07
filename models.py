"""Модели данных для базы данных"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Базовый класс для моделей
Base = declarative_base()

# Таблица Users
class User(Base):
    """Модель таблицы Users"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    posts = relationship('Post', back_populates='user')

# Таблица Posts
class Post(Base):
    """Модель таблицы Posts"""
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='posts')

# Настройки подключения к базе данных
DATABASE_URL = "postgresql://postgres:v1ctoryAppearance@localhost/python_check"
ENGINE = create_engine(DATABASE_URL)

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
