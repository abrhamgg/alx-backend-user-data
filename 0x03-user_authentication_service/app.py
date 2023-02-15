#!/usr/bin/env python3
"""main app"""
from flask import Flask, Response, abort, jsonify, make_response, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
