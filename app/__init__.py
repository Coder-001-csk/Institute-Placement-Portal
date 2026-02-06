from flask import Flask, app, render_template
from config import config
from .extensions import db, login_manager, csrf

def create_app(config_name='default'):
    """
    Application Factory Pattern
    Creates and configures the Flask application
    """
    # Create Flask app instance
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    
    # Register blueprints
    from .blueprints.auth import auth_bp
    from .blueprints.admin import admin_bp
    from .blueprints.student import student_bp
    from .blueprints.company import company_bp
    from .blueprints.api import api_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(student_bp, url_prefix='/student')
    app.register_blueprint(company_bp, url_prefix='/company')
    app.register_blueprint(api_bp, url_prefix='/api')

    
    
    # Register error handlers
    register_error_handlers(app)
    
    # Create database tables
    with app.app_context():
        db.create_all()
        # Create default admin user if not exists
        create_default_admin()
    
    return app


def register_error_handlers(app):
    """Register custom error handlers"""
    
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html'), 403
    
    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html'), 500


def create_default_admin():
    """Create default admin user if not exists"""
    from .models import User
    from werkzeug.security import generate_password_hash
    
    # Check if admin already exists
    admin = User.query.filter_by(email='admin@placementportal.edu').first()
    
    if not admin:
        admin = User(
            email='admin@placementportal.edu',
            password_hash=generate_password_hash('Admin@123'),
            role='admin',
            is_active=True
        )
        from .extensions import db
        db.session.add(admin)
        db.session.commit()
        print("✅ Default admin user created")



