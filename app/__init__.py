from flask import Flask
from app.extensions import db,login_manager,bcrypt,migrate
from app.routes.dashboard import dashboard_bp
from app.routes.health import health_bp

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='development-key'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///valentra.db'
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app,db)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(health_bp)
    return app
