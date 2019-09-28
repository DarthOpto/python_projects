from flask import Flask, abort


app = Flask(__name__)

@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return f'Hello, {user.name}'


if __name__ == '__main__':
	app.run(debug=True)