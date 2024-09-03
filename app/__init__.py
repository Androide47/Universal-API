from flask import Flask
from config import Config
from app.extensions import db, migrate, jwt, mail
from app.routes import user_routes, blog_routes, video_routes, admin_routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)

    app.register_blueprint(user_routes.bp)
    app.register_blueprint(blog_routes)
    app.register_blueprint(video_routes.bp)
    app.register_blueprint(admin_routes.bp)

    return app
