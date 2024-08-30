import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key'
    MAIL_SERVER = 'smtp.your-email-provider.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY') or 'your-stripe-api-key'
    PAYPAL_CLIENT_ID = os.environ.get('PAYPAL_CLIENT_ID') or 'your-paypal-client-id'
    PAYPAL_CLIENT_SECRET = os.environ.get('PAYPAL_CLIENT_SECRET') or 'your-paypal-client-secret'
    PAYPAL_MODE = os.environ.get('PAYPAL_MODE') or 'sandbox'