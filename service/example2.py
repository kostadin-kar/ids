import threading
import time
import logging
import random
from queue import Queue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )

BUF_SIZE = 100
q = Queue(BUF_SIZE)


class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread, self).__init__()
        self.target = target
        self.name = name

    def run(self):
        i = 0
        while True:
            i+=1
            if not q.full():
                for y in range(100):
                    q.put("{}-{}".format(i, y))
                    logging.debug('Putting ' + str(y)
                                  + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(0.8)
                # item = random.randint(1, 10)
                # q.put(item)
                # logging.debug('Putting ' + str(item)
                #               + ' : ' + str(q.qsize()) + ' items in queue')
                # time.sleep(random.random())
        return


class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread, self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        dict = {}
        dict["k"] = 2
        array = "kon".split('o')
        if dict.get(array[0]):
            print("yes be")

        while True:
            if not q.empty():
                item = q.get()
                parts = item.split('-')

                if not dict.get(parts[0]):
                    dict[parts[0]] = []
                dict[parts[0]].append(parts[1])
                logging.debug('Getting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                # time.sleep(random.random())
        return


if __name__ == '__main__':
    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')

    # time.sleep(2)
    c.start()
    p.start()

    # time.sleep(2)