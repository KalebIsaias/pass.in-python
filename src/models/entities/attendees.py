from src.models.settings.base import Base
from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.sql import func

class Attendees(Base):
  __tablename__ = "attendees"

  id = Column(String, primary_key=True)
  name = Column(String, nullable=False)
  email = Column(String, nullable=False)
  event_id = Column(String, ForeignKey("events.id"))
  created_at = Column(DateTime, default=func.now())

  def __repr__(self):
    return "Attendees [id='{}', name='{}', email='{}', event_id='{}']".format(
      self.id,
      self.name,
      self.email,
      self.event_id
    )