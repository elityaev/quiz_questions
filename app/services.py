from typing import List

import requests
from sqlalchemy import desc

from app.models import Questions
from app.schemas import QuestionScheme


def get_questions(count: int, db) -> List[QuestionScheme]:
    """
    Делает запрос к сервису https://jservice.io для получения вопросов в количестве,
    переданном на вход. Если вопрос уже есть в БД - запрашивает вместо него другой.
    """
    url = f'https://jservice.io/api/random?count={count}'
    result = requests.get(url)
    result = result.json()
    quest_list = []
    for item in result:
        exists = check_question_exists(item['id'], db)
        while exists:
            result = requests.get('https://jservice.io/api/random?count=1')
            item = result.json()[0]
            exists = check_question_exists(item['id'], db)
        question = QuestionScheme(
                question_id=item['id'],
                text=item['question'],
                answer=item['answer'],
                created_at=item['created_at']
            )
        quest_list.append(question)
    return quest_list


def create_questions(questions: List[QuestionScheme], db) -> List[Questions]:
    """
    Сохраняет объекты Question из списка в БД.
    """
    db_questions = [Questions(**question.dict()) for question in questions]
    db.add_all(db_questions)
    db.commit()
    for question in db_questions:
        db.refresh(question)
    return db_questions


def get_last_question(db) -> Questions:
    """
    Находит и возвращает последний сохраненный объект Question.
    """
    last_question = db.query(Questions).order_by(desc(Questions.id)).first()
    return last_question


def check_question_exists(question_id, db) -> bool:
    """
    Проверяет по id, существует ли в БД объект Question.
    """
    db_question = db.query(Questions).where(Questions.question_id == question_id).first()
    if db_question:
        return True
    return False
