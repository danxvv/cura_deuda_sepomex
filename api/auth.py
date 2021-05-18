from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()
user = {
    "admin": generate_password_hash("password")
}


@auth.verify_password
def verify_password(username, password):
    if username in user and check_password_hash(user.get(username), password):
        return username
