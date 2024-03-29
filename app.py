from flask import Flask, Response, request, jsonify
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

wses = []


@app.route('/')
def hello_world():  # put application's code here
    return Response('Hello World!')


@app.route('/broadcast', methods=['POST'])
def broadcast():
    data = request.json['msg']
    for ws in wses:
        try:
            ws.send(data)
        except:
            continue
    return jsonify({'success': True})


@sock.route('/getNews')
def getNews(ws):
    wses.append(ws)
    while True:
        data = ws.receive(30)
        if data:
            ws.send(data)
            wses.remove(ws)
        else:
            break


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)
