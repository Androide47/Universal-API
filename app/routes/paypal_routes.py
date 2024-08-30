from flask import Blueprint, request, jsonify, redirect, url_for
import paypalrestsdk
from config import Config

bp = Blueprint('paypal_routes', __name__)

paypalrestsdk.configure({
    "mode": Config.PAYPAL_MODE,  # sandbox or live
    "client_id": Config.PAYPAL_CLIENT_ID,
    "client_secret": Config.PAYPAL_CLIENT_SECRET
})

@bp.route('/paypal/payment', methods=['POST'])
def paypal_payment():
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://localhost:5000/paypal/payment/execute",
            "cancel_url": "http://localhost:5000/paypal/payment/cancel"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "Subscription",
                    "sku": "subscription",
                    "price": "10.00",
                    "currency": "USD",
                    "quantity": 1}]},
            "amount": {
                "total": "10.00",
                "currency": "USD"},
            "description": "Subscription payment."}]})

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return jsonify({"approval_url": link.href})
    else:
        return jsonify({"error": payment.error}), 400

@bp.route('/paypal/payment/execute', methods=['GET'])
def execute_payment():
    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return jsonify({"status": "Payment executed successfully!"})
    else:
        return jsonify({"error": payment.error}), 400

@bp.route('/paypal/payment/cancel', methods=['GET'])
def cancel_payment():
    return jsonify({"status": "Payment canceled."})
