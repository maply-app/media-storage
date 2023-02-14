from falcon.asgi import App
import mongoengine
# from falcon_multipart.middleware import MultipartMiddleware
from falcon import CORSMiddleware
from falcon.errors import (
    HTTPRouteNotFound,
    HTTPInternalServerError,
    HTTPMethodNotAllowed,
)
from middleware import UserJWT
from core.api.handlers import *
from core.api.errors import CustomException
from config import *

from api.urls import routes as api_routes

mongoengine.connect(host="mongodb://{}:{}@{}:27017/{}?authSource=admin".format(
    MONGO_USERNAME,
    MONGO_PASSWORD,
    MONGO_HOSTNAME,
    MONGO_DATABASE
))

app = App(middleware=[
    UserJWT(),
    # MultipartMiddleware(),
    CORSMiddleware(allow_origins="*", allow_credentials="*")
])

# app.API(middleware=[MultipartMiddleware()])


app.add_error_handler(CustomException, handle_custom_error)
app.add_error_handler(HTTPRouteNotFound, handle_custom_404_error)
app.add_error_handler(HTTPInternalServerError, handle_custom_500_error)
app.add_error_handler(HTTPMethodNotAllowed, handle_custom_405_error)

routes = {
    **api_routes,
}
for route in routes: 
    app.add_route(route, routes[route])