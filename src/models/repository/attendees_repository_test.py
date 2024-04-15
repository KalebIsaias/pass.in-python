import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="New Register in database")
def test_insert_attendee():
  event_id = "123"
  attendee = {
    "uuid": "456",
    "name": "Attendee 1",
    "email": "attenee@email.com",
    "event_id": event_id
  }

  attendees_repository = AttendeesRepository()
  response = attendees_repository.insert_attendee(attendee)

  print(response)

@pytest.mark.skip(reason="Not necessary")
def test_get_attendees_badge_by_id():
  attendee_id = "456"

  attendees_repository = AttendeesRepository()
  response = attendees_repository.get_attendees_badge_by_id(attendee_id)
  
  print(response)