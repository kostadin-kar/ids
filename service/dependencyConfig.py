from injector import singleton

from storyRepository import RepositoryBase
from storyRepositoryMySql import RepositoryMySql
from storyService import StoryService


def configure(binder):
    binder.bind(StoryService, to=StoryService, scope=singleton)
    binder.bind(RepositoryBase, to=RepositoryMySql, scope=singleton)
