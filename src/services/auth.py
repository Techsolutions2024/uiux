import bcrypt
from services.database import get_user, add_user

def authenticate_user(email, password):
    user = get_user(email)
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        return True
    return False

def register_user(name, email, password):
    if get_user(email):
        return False
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    add_user(name, email, hashed_password)
    return True