import flask
import VoidStorage

app = flask.Flask(__name__)

@app.route("/api/void", methods=["GET"])
def voidAPI():
	if all(elem in flask.request.args for elem in ["login", "pass", "domain", "user"]):
		login, password, domain, user = flask.request.args['login'], flask.request.args['pass'], flask.request.args['domain'], flask.request.args['user']
		return VoidStorage.voidStorage(login, password).findPassword(domain, user)
	else:
		raise ZeroDivisionError

@app.route('/<path:path>')
def send(path):
    return flask.send_from_directory('html', path)

@app.route('/')
def index():
    return flask.send_from_directory('html', 'index.html')



app.run(host='0.0.0.0',port=8080)