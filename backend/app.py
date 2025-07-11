from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import cmath
from . import rec

# uri = (URI) #need to make new cluster

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))


# app = Flask(__name__)
app = Flask(__name__, static_folder="../frontend/build/static", template_folder="../frontend/build")

CORS(app)

# db = client['Traveler']




@app.route('/')
def serve_react_app():
    return app.send_static_file('frontend/build/index.html')


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



if __name__ == '__main__':
    app.run()