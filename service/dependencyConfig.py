from injector import singleton

from storyRepository import RepositoryBase
from storyRepositoryLocal import RepositoryLocal
from storyService import StoryService


def configure(binder):
    binder.bind(StoryService, to=StoryService, scope=singleton)
    binder.bind(RepositoryBase, to=RepositoryLocal, scope=singleton)
