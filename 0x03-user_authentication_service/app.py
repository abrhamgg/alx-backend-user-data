#!/usr/bin/env python3
"""main app"""
from flask import Flask, Response, abort, jsonify, make_response, redirect
from flask import request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', strict_slashes=False)
def index():
    """defaulr route"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_user():
    """endpoint to create a user"""
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """session endpoint"""
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    res = {"email": email, "message": "logged in"}
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response(res)
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """logout function or deleting a session"""
    session_id = request.cookies.get('session_id')
    try:
        user = AUTH.get_user_from_session_id(session_id)
        AUTH.destroy_session(user.id)
        return redirect('/')
    except Exception:
        abort(403)


@app.route('/profile', strict_slashes=False)
def profile():
    """profile endpoint"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email})
    abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """function to respond to the POST /reset_password route"""
    email = request.form.get('email')
    try:
        user = AUTH._db.find_user_by(email=email)
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": user.email, "reset_token": reset_token})
    except Exception:
        abort(403)


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password() -> str:
    """PUT /reset_password
    Return:
        - The user's password updated payload.
    """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    is_password_changed = False
    try:
        AUTH.update_password(reset_token, new_password)
        is_password_changed = True
    except ValueError:
        is_password_changed = False
    if not is_password_changed:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
