# This is a placeholder for Flask + Blender integration.
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '3D Try-On API Running'

if __name__ == '__main__':
    app.run(debug=True)