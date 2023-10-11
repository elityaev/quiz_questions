from sqlalchemy import Integer, String, DateTime, Column

from app.database import Base


class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, index=True, unique=True)
    text = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)
