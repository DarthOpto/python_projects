# Volume Calculator
# A Webservice to calculate the volume of shapes

from flask import Flask, json
import web_services.volume_calculator.formulas as formulas

app = Flask(__name__)


def volume_return(shape=None, volume=None):
    ret_volume = {"shape": shape, "volume": volume}
    return json.dumps(ret_volume)


@app.route("/v1/<string:shape>/<int:measure>")
@app.route("/v1/<string:shape>/<int:measure1>/<int:measure2>")
def calculate_volume(shape=None, measure=None, measure1=None, measure2=None):
    volume = None
    if shape == "cube":
        volume = formulas.cube_volume(side=measure)
    elif shape == "sphere":
        volume = formulas.sphere_volume(radius=measure)
    elif shape == "dodecahedron":
        volume = formulas.dodecahedron_volume(side=measure)
    elif shape == "pyramid":
        volume = formulas.right_square_pyramid(base_edge=measure1, height=measure2)
    elif shape == "cylinder":
        volume = formulas.cylinder_volume(radius=measure1, height=measure2)

    return volume_return(shape=shape, volume=volume)


@app.errorhandler(500)
def internal_server_error(error):
    return str(json.dumps({"message": Exception})), 500


if __name__ == "__main__":
    app.run(debug=False)

# TODO - Add error handling that is displayed to the user
