from datetime import timedelta


#######################################################
#development

#######################################################
#JWT secret
JWT_SECRET_KEY = 'changeitlater'
JWT_COOKIE_SECURE = False  #true in production
JWT_TOKEN_LOCATION = ["cookies"]
JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=10)
JWT_COOKIE_CSRF_PROTECT = True #true in production
JWT_ACCESS_COOKIE_NAME = 'Token'
JWT_SESSION_COOKIE = False
JWT_COOKIE_SAMESITE = "Strict"
JWT_CSRF_IN_COOKIES = True #if true csrf will be saved as cookies else will remain in server and can be accessed using flask_jwt_extended.get_csrf_token()
JWT_ACCESS_CSRF_COOKIE_NAME = "Tokens"
#######################################################

