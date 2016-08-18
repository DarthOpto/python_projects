# Temperature Information
# Takes a zip code and displays temperature in all scales
# From Dark Sky API

from flask import Flask, json
import requests


app = Flask(__name__)

ZIP_API_KEY = \
    "3aZek97NfJSZFhsPDMhLHO1H2UbkEnlHykVSu2GKMzJrQbhtXyfFngmqbxKPV5wt"
DARK_SKY_API_KEY = "GET YOUR OWN DARK SKY API KEY"


def get_zip_code_info(zip_code):
    """
    Gets the Latitude and Longitude of the entered zip code
    :param zip_code: zip code
    :return: Latitude and Longitude
    """
    zip_request = requests.get(
        url="https://www.zipcodeapi.com/rest/{}/info.json/{}/degrees"
            .format(ZIP_API_KEY, zip_code))
    parsed = zip_request.json()
    latitude = parsed.get("lat")
    longitude = parsed.get("lng")
    return latitude, longitude


def get_current_temp(zip_code):
    """
    Gets the Current Temperature for the give zip code.
    :param zip_code: zip code
    :return: current temperature
    """
    latitude = get_zip_code_info(zip_code=zip_code)[0]
    longitude = get_zip_code_info(zip_code=zip_code)[1]
    temp_request = requests.get(
        url="https://api.forecast.io/forecast/{}/{},{}"
            .format(DARK_SKY_API_KEY, latitude, longitude))
    parsed = temp_request.json()
    current = parsed.get("currently")
    temperature = current.get("temperature")
    return temperature


def temperature_return(fahrenheit=None, celsius=None, kelvin=None):
    ret_temp = {"fahrenheit": fahrenheit, "celsius": celsius, "kelvin": kelvin}
    return json.dumps(ret_temp)


@app.route("/converted_temp/v1/<string:zipcode>")
def converted_temp(zipcode=None):
    """
    Shows the user the current temperature for their location in Fahrenheit,
    Celsius, and Kelvin
    :param zipcode: the zip code for the location
    :return: converted temperatures
    """
    temperature = float(get_current_temp(zip_code=zipcode))
    fahrenheit = temperature
    celsius = (temperature - 32) / 1.8
    kelvin = (temperature + 459.67) * 5/9
    return temperature_return(fahrenheit=fahrenheit, celsius=celsius,
                              kelvin=kelvin)

if __name__ == "__main__":
    app.run(debug=False)



