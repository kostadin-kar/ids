import http.client
import random
import traceback
from concurrent.futures import ThreadPoolExecutor
import time

from flask import Flask, request, jsonify

HOST = '127.0.0.1'
PORT = 5001

with open('./agents.txt') as f:
    AGENTS = [line.rstrip('\n') for line in f.readlines()]

executor = ThreadPoolExecutor(max_workers=3)

app = Flask(__name__)


@app.route("/dashboard", methods=['GET'])
@app.route("/", methods=['GET'])
def get_story():
    return 'Malicious intruder'


should_shut_down = True


@app.route("/dashboard", methods=['POST'])
def create_story():
    global should_shut_down
    action = request.args.get('action')
    if action == 'start' and should_shut_down:
        print('start attack')
        should_shut_down = False
        executor.submit(spam, 'Blob')
        executor.submit(spam, 'Greed')
        return jsonify({'message': 'Attack started'})
    elif action == 'stop' and not should_shut_down:
        print('stop attack')
        should_shut_down = True
        return jsonify({'message': 'Attack stopped'})

    return jsonify({'message': 'No action taken. Please provide query parameters, e.g. ?action=start/stop'})


def spam(name):
    connection = http.client.HTTPConnection(HOST, PORT)

    while not should_shut_down:
        try:
            headers = {
                'User-Agent': AGENTS[random.randint(0, len(AGENTS))],
                'Cache-Control': 'no-cache',
                'Accept-Encoding': '*',
                'Connection': 'keep-alive',
                'Keep-Alive': random.randint(1, 1000),
                'Host': HOST + str(PORT),
            }

            connection.request('GET', 'http://127.0.0.1:5001/stories', None, headers)
            response = connection.getresponse()
            print(name + ' sent a request at' + str(time.time()) + ', response is ' + str(response.getcode()))
            time.sleep(.05)
        except:
            traceback.print_exc()


def main():
    app.run(port=5002)


if __name__ == '__main__':
    main()