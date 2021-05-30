import pickle
import numpy as np


class Observer(object):
    _mini_som = None
    _kmeans = None
    _global_state = None

    CLUSTER_GOOD = 0
    CLUSTER_ABNORMAL = 1
    CLUSTER_BAD = 2

    def __init__(self, global_state):
        with open('som.pkl', 'rb') as reader:
            self._mini_som = pickle.load(reader)
        with open('kmean.pkl', 'rb') as reader:
            self._kmeans = pickle.load(reader)
        self._global_state = global_state

    def notify(self, request):
        activation = self._mini_som.activation_response(request)
        index = np.unravel_index(activation.argmax(), activation.shape)
        prediction = self._kmeans.predict([index])

        if self.CLUSTER_GOOD in prediction:
            self._global_state = 0
        elif self.CLUSTER_ABNORMAL in prediction:
            self._global_state = 1
        elif self.CLUSTER_BAD in prediction:
            self._global_state = 2
        else:
            print('Unrecognized cluster')
