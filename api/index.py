from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask<でつくった見出しだよ/h1><p>You visited: /%s</p>" % (path), mimetype="text/html")