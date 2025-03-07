from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import cipher
from config import URI
import cmath
import rec

# uri = (URI) #need to make new cluster

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))


app = Flask(__name__)

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
    reccomnendations = rec.realRecs(y, x)
    #rec.coverArtURLs(reccomnendations)
    return reccomnendations


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    return 0



if __name__ == '__main__':
    app.run()