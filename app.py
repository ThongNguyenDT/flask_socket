from flask import Flask, Response
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@app.route('/')
def hello_world():  # put application's code here
    return Response('Hello World!')





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)
