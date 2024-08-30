from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)

    from app.routes import user_routes, blog_routes, video_routes, admin_routes

    app.register_blueprint(user_routes.bp)
    app.register_blueprint(blog_routes.bp)
    app.register_blueprint(video_routes.bp)
    app.register_blueprint(admin_routes.bp)

    return app
