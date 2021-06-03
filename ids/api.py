from flask import Flask, jsonify
from flask_cors import CORS

import grpc_transformer
from mapper import Observer

app = Flask(__name__)
CORS(app)


trainedSOM = None
transformer = None
globalState = [-1]


@app.route("/state", methods=['GET'])
@app.route("/", methods=['GET'])
def get_stories():
    return jsonify({'global_state': globalState})


def load_engine():
    global globalState
    return Observer(globalState)


def start_shim(observer):
    grpc_transformer.serve(observer)


def main():
    observer = load_engine()

    start_shim(observer)

    app.run()


if __name__ == '__main__':
    main()