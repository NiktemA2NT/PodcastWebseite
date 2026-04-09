from flask import Flask, render_template
from flask_bcrypt import Bcrypt
import json
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('Podcast.html')

if __name__ == '__main__':
    # Dashboard-Server auf Port 8080
    app.run(host='0.0.0.0', port=8085, debug=True)