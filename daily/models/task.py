from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from daily.models.base import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    header_id = Column(Integer, ForeignKey('headers.id'))
    header = relationship('Header')
