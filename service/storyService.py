import os
import time
import traceback

from injector import inject
import grpc
from server_pb2_grpc import RequestsReceiverServiceStub
from server_pb2 import InfoRequest

from storyRepositoryLocal import RepositoryLocal


class StoryService:

    @inject
    def __init__(self, repo: RepositoryLocal):
        self._repo = repo
        try:
            host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
            channel = grpc.insecure_channel(
                f"{host}:50051"
            )
            self._client = RequestsReceiverServiceStub(channel)
            print('Grpc channel successfully created')
        except grpc.RpcError:
            traceback.print_exc()
            print('Grpc channel failed to create, skipping channel communication')

    def get_stories(self, request):
        agent = request.headers.get('User-Agent')

        try:
            self._client.SendRequestInfo(
                InfoRequest(agent=agent, timestamp=time.time())
            )
        except grpc.RpcError:
            print('Ids is not responding')

        return self._repo.get_stories()

    def get_story(self, story_id):
        return self._repo.get_story(story_id)

    def create_story(self, story):
        self._repo.create_story(story)

    def delete_story(self, story_id):
        self._repo.delete_story(story_id)
