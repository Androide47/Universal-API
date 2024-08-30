from flask import Blueprint, jsonify, request
from app.services.email_service import send_email

bp = Blueprint('admin_routes', __name__)


@bp.route('/admin/send-emails', methods=['POST'])
def send_mass_emails():
    data = request.get_json()
    send_email(data['subject'], data['body'])
    return jsonify({'message': 'Emails sent successfully'}), 200