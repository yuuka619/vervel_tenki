from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flaskでつくった見出しだよ</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")


if __name__ == '__main__':
    app.run(debug=True)

    #githubにデプロイしてブラウザ上で開くやつ