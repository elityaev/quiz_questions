from datetime import datetime

from pydantic import BaseModel


class ClientRequest(BaseModel):
    question_num: int


class QuestionScheme(BaseModel):
    question_id: int
    text: str
    answer: str
    created_at: datetime

    class Config:
        orm_mode = True
