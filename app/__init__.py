import os
import logging
from flask import Flask
from flask_talisman import Talisman
from whitenoise import WhiteNoise

def create_app():
    app = Flask(__name__)
    
    # Choose config based on environment
    env = os.environ.get('FLASK_ENV')
    if env == 'production':
        app.config.from_object('config.ProductionConfig')
        # Enforce secret key presence in production
        if not os.environ.get('SECRET_KEY'):
             raise ValueError("No SECRET_KEY set for production")
    else:
        app.config.from_object('config.DevelopmentConfig')

    # Security Headers (Talisman)
    # Note: 'unsafe-inline' is required for the Tailwind CDN.
    csp = {
        'default-src': ["'self'"],
        'script-src': ["'self'", "'unsafe-inline'", "https://cdn.tailwindcss.com"],
        'style-src': ["'self'", "'unsafe-inline'"],
        'img-src': ["'self'", "data:", "*"], 
    }
    
    # Initialize Talisman
    # force_https is True by default in Talisman, but we match it to our config
    is_production = app.config.get('SESSION_COOKIE_SECURE', False)
    
    # In development, we might not have HTTPS, so we disable force_https
    # unless we are sure we want to test it.
    Talisman(app, content_security_policy=csp, force_https=is_production)

    # Static File Serving (WhiteNoise)
    # Efficiently serve static files in production without needing Nginx configuration
    # Important: We must pass the prefix correctly or files won't load.
    static_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    
    # Disable autorefresh in development to prevent slow startup
    # WhiteNoise by default scans all files on startup. If you have many large images, this is slow.
    app.wsgi_app = WhiteNoise(app.wsgi_app, root=static_root, prefix='static/', autorefresh=False)

    from app import routes
    app.register_blueprint(routes.bp)

    return app
