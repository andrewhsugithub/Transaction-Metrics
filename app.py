from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    
    from routes.metrics import metric_routes
    app.register_blueprint(metric_routes)

    return app