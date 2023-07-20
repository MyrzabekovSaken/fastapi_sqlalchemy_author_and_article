from sqlalchemy.orm import Session

import models
import dtos


### Author

def get_author(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Author).offset(skip).limit(limit).all()

def get_author_by_id(db: Session, id: int):
    return db.query(models.Author).filter(models.Author.id == id).first()

def create_author(db: Session, author: dtos.AuthorInput):
    db_author = models.Author(first_name=author.first_name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def update_author(db: Session, id: int, author: dtos.AuthorInput):
    db_author = db.query(models.Author).filter(models.Author.id == id).first()
    db_author.first_name = author.first_name
    db.commit()
    db.refresh(db_author)
    return db_author

def delete_author(db: Session, id: int):
    db_author = db.query(models.Author).filter(models.Author.id == id).first()
    db.delete(db_author)
    db.commit()
    return db_author


### Article

def get_article(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Article).offset(skip).limit(limit).all()

def get_article_by_id(db: Session, id: int):
    return db.query(models.Article).filter(models.Article.id == id).first()

def create_article(db: Session, article: dtos.ArticleInput, author_id: int):
    db_article = models.Article(title=article.title, author_id=article.author_id)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def update_article(db: Session, id: int, article: dtos.ArticleInput):
    db_article = db.query(models.Article).filter(models.Article.id == id).first()
    db_article.title = article.title
    db_article.author_id = article.author_id
    db.commit()
    db.refresh(db_article)
    return db_article

def delete_article(db: Session, id: int):
    db_article = db.query(models.Article).filter(models.Article.id == id).first()
    db.delete(db_article)
    db.commit()
    return db_article
