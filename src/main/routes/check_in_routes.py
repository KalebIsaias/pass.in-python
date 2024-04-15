from flask import Blueprint, jsonify
from src.data.check_in_handler import CheckInHandler
from src.http_types.http_request import HttpRequest

check_in_route_bp = Blueprint("check_in_route_bp", __name__)

@check_in_route_bp.route("/attendees/<attendee_id>/check_in", methods=["POST"])
def create_check_in(attendee_id: str):
  check_in_handler = CheckInHandler()
  http_request = HttpRequest(
    param = {
      "attendee_id": attendee_id
    }
  )
  
  response = check_in_handler.register(http_request)
  return jsonify(response.body), response.status_code