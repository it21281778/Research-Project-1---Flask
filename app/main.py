from flask import Flask
from flask_cors import CORS

from app.routes.sentimental_routes import sentimental_blueprint
from app.routes.screenstats_routes import screenstats_blueprint
from app.routes.voice_recognition_routes import voice_bp

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Register Blueprints
app.register_blueprint(sentimental_blueprint, url_prefix="/sentiment")
app.register_blueprint(screenstats_blueprint, url_prefix="/screenstats")
app.register_blueprint(voice_bp, url_prefix="/api/voice")

# Enable CORS
CORS(app)

@app.route('/')
def index():
    return "Welcome to the AI Services API!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
