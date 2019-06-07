from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from daily.models.base import Base


class Header(Base):
    __tablename__ = 'headers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    tasks = relationship('Task', back_populates="header")
