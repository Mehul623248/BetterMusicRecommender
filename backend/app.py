from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import cipher
from config import URI
import cmath

uri = (URI) #need to make new cluster

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


app = Flask(__name__)

CORS(app)

db = client['Traveler']




@app.route('/')
def serve_react_app():
    return app.send_static_file('frontend/build/index.html')


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'username' in data and 'password' in data:
        logged_in = check_login_credentials(data['username'], data['password'])
        if logged_in:
             return jsonify({
                'login_status': True,
                'username': data['username']
            
            })
        else:
            return jsonify({
                'login_status': False
            })
    else:
        return jsonify({
            'login_status': False
        })


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    if 'username' in data and 'password' in data and 'email' in data and 'firstName' in data and 'lastName' in data:
        encrypted_password = cipher.encrypt(data['password'], 137, -1)
        output = add_user_to_database(data['firstName'], data['lastName'], data['email'], data['username'],
                                      encrypted_password)
        if output == 'Success':
            # create_personal_sessions(data['username'])
            return jsonify({
                'signup_status': True,
                'username': data['username']
            })
        else:
            error = ''
            if output == 'Failure: username exists':
                error = 'Username exists already!'
            elif output == 'Failure: email exists':
                error = 'Email exists already!'
            return jsonify({
                'signup_status': False,
                'error': error
            })
    else:
        return jsonify({
            'Error': 'ill-formed request'
        })



def check_login_credentials(username: str, password: str) -> bool:
    collection = db['Users']  # retrieve all users from database

    try:
        user = collection.find_one({  # find username that was typed in, if not found, user=null
            'username': username
        })
        email = collection.find_one({
            'email': username
        })
        if user:  # if the user was found, typed password will be checked with actual password
            encrypted_password = user['password']
            decrypted_password = cipher.decrypt(encrypted_password, 137, -1)
            if decrypted_password == password:  # if passwords match, login succeeds
                return True
            else:
                return False  # if passwords do not match, login fails
        else:  # if user is not found, login fails
            return False
    except Exception as e:
        print(str(e))
        return False


def add_user_to_database(first_name: str, last_name: str, email: str, username: str, password: str) -> str:
    collection = db['Users']  # retrieve all users from database

    if collection.find_one(
            {'username': username}) is not None:  # if username already exists, return Failure to add user
        return "Failure: username exists"
    elif collection.find_one({'email': email}) is not None:
        return "Failure: email exists"
    else:  # user does not exist in database...
        try:
            collection.insert_one({  # add all necessary credentials to login
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'username': username,
                'password': password
            })
        except Exception as e:
            return str(e)
    return "Success"

def create_personal_sessions(username: str) -> bool:  # Initializes a new user's account by creating an empty
    # dictionary entitled 'sessions'
    personal_data = db['Users']

    try:
        personal_data.insert_one({
            'username': username,
            
        }
        )
        print(f"Successfully created an account for {username}")
    except Exception as e:
        print(str(e))
        return False

    return True

if __name__ == '__main__':
    app.run()