from sre_constants import OP_IGNORE
from web import app, jwt
from flask_jwt_extended import create_access_token, get_csrf_token, unset_access_cookies, get_current_user, jwt_required, set_access_cookies, get_jwt, get_jwt_identity, unset_jwt_cookies, verify_jwt_in_request
from flask_restful import Resource
from flask import request, jsonify
from datetime import datetime, timedelta


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now()
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity='admin')
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response


class Home(Resource):
    def get(self):
        return {'message': 'this is home, no user authentication required'}

class Login(Resource):
    def post(self):
        data = request.get_json() 
        if data['email'] == 'admin@admin.com' and data['password'] == 'adminpassword':
            access_token=create_access_token(identity=data['email'])
            response = jsonify({'message': 'You are logged in as admin'})
            set_access_cookies(response, access_token)
            return response
        else:
            return {'message': 'invalid credentials'}
 
class Logout(Resource):
    @jwt_required()         #to confirm if the user is authenticated
    def post(self):
        response = jsonify({'message':"Successfully Logged Out"}) 
        unset_jwt_cookies(response)
        return response

class Test(Resource):
    @jwt_required()
    def get(self):
        return {'message': 'this is test, user authentication required'}

