# call repo and send data to ids
import os
import time

from injector import inject
from http import client
from json import dumps
import grpc
from server_pb2_grpc import RequestsReceiverServiceStub
from server_pb2 import InfoRequest

from storyRepository import RepositoryBase

host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
channel = grpc.insecure_channel(
    f"{host}:50051"
)
client = RequestsReceiverServiceStub(channel)


class StoryService:

    @inject
    def __init__(self):
        # self.headers = {'Content-type': 'application/json'}
        # self.connection = client.HTTPSConnection('gimmi url')
        print(f"Initializing DatabaseBase instance ")

    def get_stories(self, request):
        agent = request.headers.get('User-Agent')  #'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        # body = {'method': 'GET', 'time': time.time(), 'ip': request.remote_addr}
        # json_body = dumps(body)

        # platform = request.user_agent.platform
        # browser = request.user_agent.browser
        # version = request.user_agent.version
        # engine = request.user_agent.string

        client.SendRequestInfo(
            InfoRequest(agent=agent, timestamp=time.time())
        )
        client.SendRequestInfo(
            InfoRequest(agent=agent, timestamp=time.time())
        )
        # self.connection.request('POST', '/analyze', json_body, self.headers)
        # response = self.connection.getresponse()
        return ["a", "n"]


    def get_story(self, story_id):
        return "ID-" + story_id


    def create_story(self, story):
        return "created"


    def delete_story(self, story_id):
        return "deleted"
