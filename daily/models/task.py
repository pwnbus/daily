from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from daily.models.base import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    header_id = Column(Integer, ForeignKey('headers.id'))
    header = relationship('Header')
    completed = Column(Boolean, default=False)
    completed_at = Column(String(50), nullable=True)

    def status(self):
        if self.completed:
            return "complete"
        else:
            return "incomplete"
