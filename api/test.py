from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "helloWorld!!!"


if __name__ == "__main__":
    app.ron()