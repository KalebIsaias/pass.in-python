from src.models.settings.base import Base
from sqlalchemy import Column, Integer, String

class Events(Base):
  __tablename__ = "events"

  id = Column(String, primary_key=True)
  title = Column(String, nullable=False) 
  details = Column(String)
  slug = Column(String, nullable=False)
  maximum_attendees = Column(Integer)

  def __repr__(self):
    return "Events [id='{}', title='{}', slug='{}', maximum_attendees='{}']".format(
      self.id,
      self.title,
      self.slug,
      self.maximum_attendees
    )