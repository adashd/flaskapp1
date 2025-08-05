from flask import Flask

app = Flask(__name__)

@app.route("/")
def AD():
	return "This app is running in my server\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
