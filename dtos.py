from pydantic import BaseModel, Field

class AuthorInput(BaseModel):
    first_name: str = Field(..., min_length=3, max_length=50)

class Author(AuthorInput):
    id: int
    first_name: str

    class Config:
        orm_mode = True

class ArticleInput(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    author_id: int = Field(..., gt=0)

class Article(ArticleInput):
    id: int
    title: str
    author_id: int

    class Config:
        orm_mode = True
