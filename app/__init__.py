from flask import Flask

from app.extensions import db, login_manager, bcrypt, migrate
from app.models.user import User
from app.routes.dashboard import dashboard_bp
from app.routes.health import health_bp
from app.auth.routes import auth_bp


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'development-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///valentra.db'

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)

    return app