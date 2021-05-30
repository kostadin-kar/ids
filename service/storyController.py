from flask import Flask, jsonify, request
from flask_injector import FlaskInjector
from injector import inject

from dependencyConfig import configure
from storyService import StoryService

app = Flask(__name__)


@inject
@app.route("/stories", methods=['GET'])
@app.route("/", methods=['GET'])
def get_stories(service: StoryService):
    stories = service.get_stories(request)
    return jsonify(stories)


@inject
@app.route("/stories/<story_id>", methods=['GET'])
def get_story(story_id, service: StoryService):
    story = service.get_story(story_id)
    return jsonify(story)


@inject
@app.route("/stories", methods=['POST'])
def create_story(service: StoryService):
    result = service.create_story({})
    return jsonify(result)


@inject
@app.route("/stories/<story_id>", methods=['DELETE'])
def delete_story(story_id, service: StoryService):
    result = service.delete_story(story_id)
    return result


FlaskInjector(app=app, modules=[configure])


def main():
    app.run(port=5001)


if __name__ == '__main__':
    main()
