from flask import Blueprint, request, jsonify
import stripe
from app import db
from app.models import User
from config import Config

bp = Blueprint('payment_routes', __name__)

stripe.api_key = Config.STRIPE_API_KEY

@bp.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    data = request.get_json()
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Subscription',
                    },
                    'unit_amount': 1000,  # Amount in cents
                },
                'quantity': 1,
            }],
            mode='subscription',
            success_url='https://your-domain.com/success',
            cancel_url='https://your-domain.com/cancel',
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403
