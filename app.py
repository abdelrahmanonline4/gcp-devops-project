from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

# Initialize the Flask application
app = Flask(__name__)

# Set up logging
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

@app.route('/')
def hello_world():
    app.logger.info('Hello World endpoint was hit')
    return 'Hello, welcome to a simplified Flask application for DevOps by abdelrahman ahmed !'

if __name__ == '__main__':
    # Run the app on all interfaces on port 5000
    app.run(host='0.0.0.0', port=5000)
