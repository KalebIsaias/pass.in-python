from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendees_handler import AttendeesHandler

attendees_route_bp = Blueprint('attendees_route', __name__)

@attendees_route_bp.route('/events/<event_id>/register', methods=['POST'])
def create_attendee(event_id: str):
  attendees_handler = AttendeesHandler()
  http_request = HttpRequest(
    param={ "event_id": event_id },
    body=request.json,
  )

  response = attendees_handler.register(http_request)
  return jsonify(response.body), response.status_code

@attendees_route_bp.route('/attendees/<attendee_id>/badge', methods=['GET'])
def find_attendee_badge(attendee_id: str):
  attendees_handler = AttendeesHandler()
  http_request = HttpRequest(
    param={ "attendee_id": attendee_id },
    body=None,
  )

  response = attendees_handler.find_attendee_badge(http_request)
  return jsonify(response.body), response.status_code

@attendees_route_bp.route('/events/<event_id>/attendees', methods=['GET'])
def get_attendees(event_id: str):
  attendees_handler = AttendeesHandler()
  http_request = HttpRequest(
    param={ "event_id": event_id },
  )

  response = attendees_handler.find_attendees_from_event(http_request)
  return jsonify(response.body), response.status_code