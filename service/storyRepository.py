# interface and sory entity, other class will be sql implementation detail
from abc import ABC, abstractmethod


class RepositoryBase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        pass
