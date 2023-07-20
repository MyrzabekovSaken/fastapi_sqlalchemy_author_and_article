from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, index=True)

    article = relationship("Article", back_populates="author")


class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("author.id"))

    author = relationship("Author", back_populates="article")

