from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

app = Flask(__name__)

app.config.from_pyfile('config.py')

api=Api(app)

jwt = JWTManager(app)


from web.main.views import Home, Login, Logout, Test

api.add_resource(Home, '/api/home')
api.add_resource(Login, '/api/login')
api.add_resource(Logout, '/api/logout')
api.add_resource(Test, '/api/test')