from asyncio import Queue
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor
import time

import grpc
from server_pb2_grpc import RequestsReceiverServiceServicer
import server_pb2_grpc
from google.protobuf import empty_pb2

queue = Queue(100)


class RequestsReceiverService(RequestsReceiverServiceServicer):
    def SendRequestInfo(self, request, context):
        print(request)
        while True:
            if not queue.full():
                queue.put({request.agent, request.timestamp})
                return empty_pb2.Empty()
                break
            else:
                time.sleep(1)


class Transformer(object):
    _observer = None

    def __init__(self, observer):
        self._observer = observer

    def transform(self):
        buffer = []
        print('Starting infinite transfformer loop')

        while True:
            if not queue.empty():
                item = queue.get()
                if len(buffer) == 0:
                    buffer.append(item)
                elif int(buffer[0].timestamp) == int(item.timestamp):
                    buffer.append(item)
                else:
                    ips = set()
                    for b in buffer:
                        ips.add(b.agent)

                    self._observer.notify([[len(ips), len(buffer)]])
                    buffer.clear()
                    buffer.append(item)
            else:
                time.sleep(1)


def init_grpc_server():
    print('Im initializing grpc server')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    server_pb2_grpc.add_RequestsReceiverServiceServicer_to_server(
        RequestsReceiverService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print('Finished initializing grpc server')

    server.wait_for_termination()


def serve(observer):
    transformer = Transformer(observer)

    executor = ThreadPoolExecutor(max_workers=2)
    # with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(init_grpc_server)
    executor.submit(transformer.transform)


# if __name__ == "__main__":
#     serve()

# extensions for the future: different request methods,