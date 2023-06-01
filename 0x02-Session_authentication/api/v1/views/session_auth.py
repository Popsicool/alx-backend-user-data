#!/usr/bin/env python3
"""
handles all routes for the Session authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def view_auth_sec() -> str:
    """
    Authenticate user
    """
    email = request.form.get("email", None)
    password = request.form.get("password", None)
    if email is None or len(email) < 1:
        return jsonify({"error": "email missing"}), 400
    if password is None or len(password) < 1:
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})

    if len(users) < 1:
        return jsonify({"error": "no user found for this email"}), 400
    from api.v1.app import auth
    for user in users:
        if user.is_valid_password(password):
            session_id = auth.create_session(user.id)
            res = jsonify(user.to_json())
            res.set_cookie("_my_session_id", session_id)
            return res
    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def view_logout() -> str:
    '''
    delete
    '''
    from api.v1.app import auth
    logout = auth.destroy_session(request)
    if not logout:
        abort(404)
    return jsonify({}), 200
