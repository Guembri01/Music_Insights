from flask import Flask
from flask_caching import Cache

# Configure caching
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})  # Use 'SimpleCache' for development

def create_app():
    app = Flask(__name__)
    cache.init_app(app)  # Initialize Flask-Caching

    # Configuration (if needed)
    # app.config['SECRET_KEY'] = 'your_secret_key'  # For sessions, etc.

    # Import and register blueprints (for modularity)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app