#!/usr/bin/env python3
"""
Main module
"""


from flask import Flask, jsonify
from flask import request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def home() -> str:
    """Home endpoint
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    """Users endpoint
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """Login endpoint
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        return jsonify({"message": "wrong password"}), 401


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """Logout endpoint
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        return jsonify({"message": "Unauthorized"}), 403
    AUTH.destroy_session(user.id)
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
