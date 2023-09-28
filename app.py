#import requests
#import zipcodes
from flask import Flask, Response, make_response
from flask_smorest import Api

from resources.weather import blp as WeatherBlueprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "NWS REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = \
    "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

#api_base = "https://api.weather.gov"

api = Api(app)

api.register_blueprint(WeatherBlueprint)
#def geocode(zip) -> tuple:
#    if zipcodes.is_real(zip):
#        zip_nfo = zipcodes.matching(zip)[0]
#        return (zip_nfo["lat"], zip_nfo["long"])
#    else:
#        return False
#
#
#def get_weather(zip) -> Response:
#    endpoint = "points"
#    coord = geocode(str(zip))
#    if coord:
#        req_url = f"{api_base}/{endpoint}/{coord[0]},{coord[1]}"
#        loc_info = requests.get(req_url)
#        forecast_url = loc_info.json()["properties"]["forecast"]
#        forecast_info = requests.get(forecast_url)
#        return forecast_info
#    else:
#        return Response("Zipcode not found.", status=400,
#                        mimetype='application/json')
#
#
#@app.get("/weather/<string:zip>/now")
#def get_weather_now(zip):
#    loc_weather_now = get_weather(zip)
#    resp = make_response(loc_weather_now.json()["properties"]["periods"][0],
#                         201)
#    resp.headers["Content-Type"] = 'application/json'
#    return resp
#
#
#@app.get("/weather/<string:zip>/temperature")
#def get_temp(zip):
#    weather = get_weather(zip)
#    resp = make_response(str(weather.json()["properties"]["periods"][0]
#                             ["temperature"]), 201)
#    resp.headers["Content-Type"] = 'text/plain'
#    return resp
#