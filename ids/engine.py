from math import sqrt
from warnings import warn

from numpy import (array, unravel_index, nditer, linalg, random, subtract, power, exp, zeros, arange, meshgrid, dot,
                   einsum, sqrt, argmin)
from numpy.linalg import norm


def _build_iteration_indexes(data_len, num_iterations, random_generator=None):
    iterations = arange(num_iterations) % data_len
    if random_generator:
        random_generator.shuffle(iterations)

    return iterations


def asymptotic_decay(learning_rate, t, max_iter):
    return learning_rate / (1+t/(max_iter/2))


class MiniSom(object):
    def __init__(self, x, y, input_len, sigma=1.0, learning_rate=0.5,
                 decay_function=asymptotic_decay,
                 neighborhood_function='gaussian', topology='rectangular',
                 activation_distance='euclidean', random_seed=None):

        if sigma >= x or sigma >= y:
            warn('Warning: sigma is too high for the dimension of the map.')

        self._random_generator = random.RandomState(random_seed)

        self._learning_rate = learning_rate
        self._sigma = sigma
        self._input_len = input_len
        # random initialization
        self._weights = self._random_generator.rand(x, y, input_len)*2-1
        self._weights /= linalg.norm(self._weights, axis=-1, keepdims=True)

        self._activation_map = zeros((x, y))
        self._neigx = arange(x)
        self._neigy = arange(y) # used to evaluate the neighborhood function

        if topology not in ['hexagonal', 'rectangular']:
            msg = '%s not supported only hexagonal and rectangular available'
            raise ValueError(msg % topology)
        self.topology = topology
        self._xx, self._yy = meshgrid(self._neigx, self._neigy)
        self._xx = self._xx.astype(float)
        self._yy = self._yy.astype(float)

        self._decay_function = decay_function

        neig_functions = {'gaussian': self._gaussian}

        if neighborhood_function not in neig_functions:
            msg = '%s not supported. Functions available: %s'
            raise ValueError(msg % (neighborhood_function,
                                    ', '.join(neig_functions.keys())))

        self.neighborhood = neig_functions[neighborhood_function]

        distance_functions = {'euclidean': self._euclidean_distance}

        if activation_distance not in distance_functions:
            msg = '%s not supported. Distances available: %s'
            raise ValueError(msg % (activation_distance,
                                    ', '.join(distance_functions.keys())))

        self._activation_distance = distance_functions[activation_distance]

    def get_weights(self):
        return self._weights
    
    def _activate(self, x):
        self._activation_map = self._activation_distance(x, self._weights)

    def _gaussian(self, c, sigma):
        d = 2*sigma*sigma
        ax = exp(-power(self._xx-self._xx.T[c], 2)/d)
        ay = exp(-power(self._yy-self._yy.T[c], 2)/d)
        return (ax * ay).T  # the external product gives a matrix
    
    def _euclidean_distance(self, x, w):
        return linalg.norm(subtract(x, w), axis=-1)
    
    def _check_iteration_number(self, num_iteration):
        if num_iteration < 1:
            raise ValueError('num_iteration must be > 1')

    def _check_input_len(self, data):
        data_len = len(data[0])
        if self._input_len != data_len:
            msg = 'Received %d features, expected %d.' % (data_len, self._input_len)
            raise ValueError(msg)
    
    def winner(self, x):
        self._activate(x)
        return unravel_index(self._activation_map.argmin(), self._activation_map.shape)
    
    def update(self, x, win, t, max_iteration):
        eta = self._decay_function(self._learning_rate, t, max_iteration)
        # sigma and learning rate decrease with the same rule
        sig = self._decay_function(self._sigma, t, max_iteration)
        # improves the performances
        g = self.neighborhood(win, sig)*eta
        # w_new = eta * neighborhood_function * (x-w)
        self._weights += einsum('ij, ijk->ijk', g, x-self._weights)
    
    def quantization(self, data):
        self._check_input_len(data)
        winners_coords = argmin(self._distance_from_weights(data), axis=1)
        return self._weights[unravel_index(winners_coords, self._weights.shape[:2])]
    
    def random_weights_init(self, data):
        self._check_input_len(data)
        it = nditer(self._activation_map, flags=['multi_index'])
        while not it.finished:
            rand_i = self._random_generator.randint(len(data))
            self._weights[it.multi_index] = data[rand_i]
            it.iternext()
    
    def train(self, data, num_iteration, random_order=False, verbose=False):
        self._check_iteration_number(num_iteration)
        self._check_input_len(data)
        random_generator = None
        if random_order:
            random_generator = self._random_generator
        iterations = _build_iteration_indexes(len(data), num_iteration,
                                              verbose, random_generator)
        for t, iteration in enumerate(iterations):
            self.update(data[iteration], self.winner(data[iteration]),
                        t, num_iteration)
        if verbose:
            print('\n quantization error:', self.quantization_error(data))
    
    def activation_response(self, data):
        self._check_input_len(data)
        a = zeros((self._weights.shape[0], self._weights.shape[1]))
        for x in data:
            a[self.winner(x)] += 1
        return a
    
    def _distance_from_weights(self, data):
        input_data = array(data)
        weights_flat = self._weights.reshape(-1, self._weights.shape[2])

        input_data_sq = power(input_data, 2).sum(axis=1, keepdims=True)
        weights_flat_sq = power(weights_flat, 2).sum(axis=1, keepdims=True)
        cross_term = dot(input_data, weights_flat.T)
        return sqrt(-2 * cross_term + input_data_sq + weights_flat_sq.T)
    
    def quantization_error(self, data):
        self._check_input_len(data)
        return norm(data-self.quantization(data), axis=1).mean()
