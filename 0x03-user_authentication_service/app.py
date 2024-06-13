#!/usr/bin/env python3
"""
Main module
"""


from flask import Flask, jsonify
from flask import request
from auth import Auth


app = Flask(__name__)
# AUTH = Auth()


@app.route('/')
def home() -> str:
    """Home endpoint
    """
    return jsonify({"message": "Bienvenue"})


# @app.route('/users', methods=['POST'])
# def users() -> str:
#     """Users endpoint
#     """
#     email = request.form.get('email')
#     password = request.form.get('password')
#     try:
#         AUTH.register_user(email, password)
#         return jsonify({"email": email, "message": "user created"})
#     except ValueError:
#         return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
