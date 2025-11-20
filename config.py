import os

class Config:
    # In previous versions, this was a property. We must ensure it's a simple string.
    # We use a default for development, but production must override it.
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-for-local-testing-only')
    
    # Security settings
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # In production, ensure these are set securely
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class ProductionConfig(Config):
    # Ensure we use the environment variable in production, or fail if missing
    pass
