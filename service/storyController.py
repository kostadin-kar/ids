from flask import Flask, jsonify, request
from flask_injector import FlaskInjector
from injector import inject
from flask_cors import CORS

from dependencyConfig import configure
from storyService import StoryService

app = Flask(__name__)
CORS(app)


@inject
@app.route("/stories", methods=['GET'])
@app.route("/", methods=['GET'])
def get_stories(service: StoryService):
    stories = service.get_stories(request)
    return jsonify(stories)


@inject
@app.route("/stories/<story_id>", methods=['GET'])
def get_story(story_id, service: StoryService):
    story = service.get_story(int(story_id))
    return jsonify(story)


@inject
@app.route("/stories", methods=['POST'])
def create_story(service: StoryService):
    print('POST request')
    body = request.json
    service.create_story(body)
    return jsonify(202)


@inject
@app.route("/stories/<story_id>", methods=['DELETE'])
def delete_story(story_id, service: StoryService):
    print('delete request')

    service.delete_story(int(story_id))
    return jsonify(201)


FlaskInjector(app=app, modules=[configure])


def main():
    app.run(port=5001)


if __name__ == '__main__':
    main()
