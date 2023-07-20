from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

import service
import models
import dtos
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


### Author

@app.get("/authors", response_model=list[dtos.Author])
def get_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_author(db, skip, limit)

@app.get("/authors/{id}", response_model=dtos.Author)
def get_author_by_id(id: int, db: Session = Depends(get_db)):
    author = service.get_author_by_id(db, id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@app.post("/authors", response_model=dtos.Author, status_code=201)
def create_author(author: dtos.AuthorInput, db: Session = Depends(get_db)):
    return service.create_author(db, author)

@app.put("/authors/{id}", response_model=dtos.Author)
def update_author(id: int, author: dtos.AuthorInput, db: Session = Depends(get_db)):
    return service.update_author(db, id, author)

@app.delete("/authors/{id}", response_model=dtos.Author)
def delete_author(id: int, db: Session = Depends(get_db)):
    return service.delete_author(db, id)


### Article

@app.get("/articles", response_model=list[dtos.Article])
def get_articles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_article(db, skip, limit)

@app.get("/articles/{id}", response_model=dtos.Article)
def get_article_by_id(id: int, db: Session = Depends(get_db)):
    article = service.get_article_by_id(db, id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@app.post("/articles", response_model=dtos.Article, status_code=201)
def create_article(article: dtos.ArticleInput, db: Session = Depends(get_db)):
    return service.create_article(db, article, article.author_id)

@app.put("/articles/{id}", response_model=dtos.Article)
def update_article(id: int, article: dtos.ArticleInput, db: Session = Depends(get_db)):
    return service.update_article(db, id, article)

@app.delete("/articles/{id}", response_model=dtos.Article)
def delete_article(id: int, db: Session = Depends(get_db)):
    return service.delete_article(db, id)
