import bcrypt
import secrets
import logging
from services.database import get_user, add_user, store_password_reset_token, get_user_by_reset_token, update_user_password

logger = logging.getLogger("auth")

def authenticate_user(email, password):
    user = get_user(email)
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        logger.info(f"User authenticated: {email}")
        return True
    logger.warning(f"Failed authentication attempt: {email}")
    return False

def register_user(name, email, password):
    if get_user(email):
        logger.warning(f"Registration attempt with existing email: {email}")
        return False
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    add_user(name, email, hashed_password)
    logger.info(f"User registered: {email}")
    return True

def send_password_reset_email(email):
    user = get_user(email)
    if not user:
        return False
    # Generate secure token
    token = secrets.token_urlsafe(32)
    # Store token with user in database
    store_password_reset_token(user['id'], token)
    # TODO: Implement actual email sending with token link
    logger.info(f"Password reset token generated for {email}: {token}")
    return True

def reset_password(token, new_password):
    user = get_user_by_reset_token(token)
    if not user:
        logger.warning(f"Invalid password reset token used: {token}")
        return False
    hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    update_user_password(user['id'], hashed_password)
    logger.info(f"Password reset successful for user: {user['email']}")
    return True
