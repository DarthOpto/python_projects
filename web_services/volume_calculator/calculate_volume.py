# Volume Calculator
# A Webservice to calculate the volume of shapes

from flask import Flask, json
from web_services.volume_calculator.formulas import Formulas as formulas

app = Flask(__name__)

def volume_return(shape=None, volume=None):
    ret_volume = {"shape": shape, "volume": volume}
    return json.dumps(ret_volume)


@app.route("/v1/<string:shape>/<int:measure>")
def calculate_volume(shape=None, measure=None):
    volume = None
    if shape == "cube":
        volume = formulas.cube_volume(measure)
    elif shape == "sphere":
        volume = formulas.sphere_volume(measure)

    return volume_return(shape=shape, volume=volume)

if __name__ == "__main__":
    app.run(debug=False)
