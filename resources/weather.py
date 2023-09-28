import requests
import zipcodes
from flask import Response, make_response
from flask.views import MethodView
from flask_smorest import Blueprint

blp = Blueprint("weather", __name__, description="NWS weather API operations")

api_base = "https://api.weather.gov"


def geocode(zip) -> tuple:
    if zipcodes.is_real(zip):
        zip_nfo = zipcodes.matching(zip)[0]
        return (zip_nfo["lat"], zip_nfo["long"])
    else:
        return False


def get_weather(zip) -> Response:
    endpoint = "points"
    coord = geocode(str(zip))
    if coord:
        req_url = f"{api_base}/{endpoint}/{coord[0]},{coord[1]}"
        loc_info = requests.get(req_url)
        forecast_url = loc_info.json()["properties"]["forecast"]
        forecast_info = requests.get(forecast_url)
        return forecast_info
    else:
        return Response("Zipcode not found.", status=400,
                        mimetype='application/json')


@blp.route("/weather/<string:zip>/temperature")
class NWSWeatherTemp(MethodView):
    def get(self, zip):
        weather = get_weather(zip)
        resp = make_response(str(weather.json()["properties"]["periods"][0]
                             ["temperature"]), 201)
        resp.headers["Content-Type"] = 'text/plain'
        return resp


@blp.route("/weather/<string:zip>/now")
class NWSWeatherNow(MethodView):
    def get(self, zip):
        loc_weather_now = get_weather(zip)
        resp = make_response(loc_weather_now.json()["properties"]
                             ["periods"][0], 201)
        resp.headers["Content-Type"] = 'application/json'
        return resp
