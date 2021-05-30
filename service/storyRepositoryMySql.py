from storyRepository import RepositoryBase


class RepositoryMySql(RepositoryBase):

    def __init__(self):
        super().__init__()

    def connect(self):
        pass
