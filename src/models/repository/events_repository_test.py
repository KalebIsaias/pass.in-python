import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="New Register in database")
def test_insert_event():
  event = {
    "uuid": "123",
    "title": "Event 1",
    "details": "Details of event 1",
    "slug": "event-1",
    "maximum_attendees": 10
  }

  events_repository = EventsRepository()
  response = events_repository.insert_event(event)
  print(response)

# @pytest.mark.skip(reason="Not necessary")
def test_get_event_by_id():
  events_repository = EventsRepository()
  response = events_repository.get_event_by_id("123")
  print(response)