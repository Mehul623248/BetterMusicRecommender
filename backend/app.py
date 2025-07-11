from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import cmath
from . import rec
import os

# uri = (URI) #need to make new cluster

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))


# app = Flask(__name__)




# CORS(app)


current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the project root directory (one level up from 'backend')
project_root = os.path.join(current_dir, '..')
# Path to your React build folder
REACT_BUILD_DIR = os.path.join(project_root, 'frontend', 'build')

app = Flask(__name__, static_folder=REACT_BUILD_DIR , static_url_path='/')  # Tell Flask where to find static files

CORS(app)



@app.route('/')
def serve_react_app():

    return send_from_directory(app.static_folder, 'index.html') #app.send_static_file('frontend/build/index.html')


@app.route('/getRecs', methods=['POST'])
def login():
    data = request.get_json()
    entry = data['songs']
    for i in range(len(entry)):
        entry[i] = entry[i].replace(" by ", ";")
    print(entry)

    rec.getPlaylistInfo(entry)
    x=  rec.moreProcessTags()
    rec.youTube(x)
    y= rec.recs()
    reccomendations = rec.realRecs(y, x)
    imgs = rec.coverArtURLs(reccomendations)
    return [reccomendations, imgs]


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    return 0

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run()