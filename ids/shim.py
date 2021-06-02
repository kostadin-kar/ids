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
                queue.put_nowait({'agent': request.agent, 'timestamp': request.timestamp})
                return empty_pb2.Empty()
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
                item = queue.get_nowait()
                print(item)
                if len(buffer) == 0:
                    buffer.append(item)
                elif int(buffer[0].get('timestamp')) == int(item.get('timestamp')):
                    buffer.append(item)
                else:
                    ips = set()
                    for b in buffer:
                        ips.add(b.get('agent'))

                    print('Notifying observer')
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
    executor.submit(init_grpc_server)
    executor.submit(transformer.transform)
