from typing import Annotated, Union

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models
from app.services import get_questions, create_questions, get_last_question
from app.database import engine, SessionLocal
from app.schemas import ClientRequest, QuestionScheme

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post('/', response_model=Union[QuestionScheme, None])
def request_questions(client_request: ClientRequest, db: db_dependency):
    last_question = get_last_question(db)
    data = get_questions(client_request.question_num, db)
    create_questions(data, db)
    return last_question
