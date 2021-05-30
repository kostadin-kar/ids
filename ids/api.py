from flask import Flask, jsonify, request
import shim
from mapper import Observer

app = Flask(__name__)


trainedSOM = None
transformer = None
globalState = None


def load_engine():
    return Observer(globalState)


def start_shim(observer):
    shim.serve(observer)


def main():
    observer = load_engine()

    start_shim(observer)

    app.run()


if __name__ == '__main__':
    main()