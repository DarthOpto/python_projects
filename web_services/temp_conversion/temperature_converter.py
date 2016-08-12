# Temperature Converter
# A webservice to convert temperatures


from flask import Flask, json


app = Flask(__name__)


def temperature_return(scale=None, temperature=None, converted_scale=None,
                       converted_temp=None):
    ret_temp = {"scale": scale, "temperature": temperature,
                "converted_scale": converted_scale,
                "converted_temp": converted_temp}
    return json.dumps(ret_temp)


@app.route("/temp_conversion/v1/<string:converter>/<int:temp>")
def convert_temperature(converter=None, temp=None):
    """
    Take a temperature and convert it.
    FtoC = Fahrenheit to Celsius
    CtoF = Celsius to Fahrenheit
    FtoK = Fahrenheit to Kelvin
    KtoF = Kelvin to Fahrenheit
    CtoK = Celsius to Kelvin
    :param converter: which conversion user wants to use
    :param temp: Float value of the temperature
    :return: Conversion based on path
    """
    scale = None
    temperature = float(temp)
    converted_scale = None
    converted_temp = None

    if converter == "FtoC":
        scale = "Fahrenheit"
        converted_scale = "Celsius"
        converted_temp = (temp - 32) / 1.8
    elif converter == "CtoF":
        scale = "Celsius"
        converted_scale = "Fahrenheit"
        converted_temp = (temp * 1.8) + 32
    elif converter == "FtoK":
        scale = "Fahrenheit"
        converted_scale = "Kelvin"
        converted_temp = (temp + 459.67) * 5/9
    elif converter == "KtoF":
        scale = "Kelvin"
        converted_scale = "Fahrenheit"
        converted_temp = (temp * 9/5) - 459.67
    elif converter == "CtoK":
        scale = "Celsius"
        converted_scale = "Kelvin"
        converted_temp = temp + 273.15
    elif converter == "KtoC":
        scale = "Kelvin"
        converted_scale = "Celsius"
        converted_temp = temp - 273.15
    return temperature_return(scale=scale, temperature=temperature,
                              converted_scale=converted_scale,
                              converted_temp=converted_temp)


@app.errorhandler(500)
def internal_server_error(error):
    return str(json.dumps({"message": "There is a problem with the "
                                      "server"})), 500


@app.errorhandler(404)
def page_not_found(error):
    return str(json.dumps(
        {"message": "There is a problem with the URL you typed in. "
                    "It must look like this: "
                    "http://IP:PORT/temp_conversion/v1/converter"
                    "/temperature. The converter must be one of the "
                    "following: FtoC, CtoF, FtoK, KtoF, CtoK, KtoC"})), 404


if __name__ == "__main__":
    app.run(debug=False)
