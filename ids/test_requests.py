
import numpy as np
# import matplotlib.pyplot as plt
from sklearn import preprocessing as prep
import pickle

from engine import MiniSom

np.random.RandomState(10)
N_points = 40
N_neurons = N_points*2
# t = np.linspace(0, np.pi*2, N_points)
# x = np.cos(t)+(np.random.rand(N_points)-.5)*.3
# y = np.sin(t)+(np.random.rand(N_points)-.5)*.3
x = [3, 1, 2, 4, 2, 1, 12, 17, 24, 27, 26, 25, 3, 1, 2, 2, 1, 3, 14, 19, 29, 37, 38, 52, 58, 77, 16, 12, 11, 7]
y = [4, 2, 2, 6, 3, 1, 15, 25, 39, 47, 51, 42, 7, 1, 4, 3, 1, 4, 17, 19, 34, 41, 55, 134, 167, 228, 34, 21, 13, 9]

som = MiniSom(8, 10, 2, sigma=8, learning_rate=.4,
              neighborhood_function='gaussian', random_seed=0)
points = np.array([x,y]).T
som.random_weights_init(points)

# plt.figure(figsize=(10, 9))
for i, iterations in enumerate(range(5, 61, 5)):
    som.train(points, iterations, verbose=False, random_order=False)
    # plt.subplot(3, 4, i+1)
    # plt.scatter(x,y)
    # visit_order = np.argsort([som.winner(p)[1] for p in points])
    # visit_order = np.concatenate((visit_order, [visit_order[0]]))
    #
    # plt.plot(points[visit_order][:,0], points[visit_order][:,1])
    # plt.title("iterations: {i};\nerror: {e:.3f}".format(i=iterations,
    #                                                     e=som.quantization_error(points)))
    # plt.xticks([])
    # plt.yticks([])

with open('som.pkl', 'wb') as picklerSom:
    pickle.dump(som, picklerSom)

with open('som.pkl', 'rb') as picklerSom:
    pickledSom = pickle.load(picklerSom)
    print(som == pickledSom)


# # ========
# def draw2():
#     for i in points:
#         res2 = som.activation_response([i])
#         resIndex = np.unravel_index(res2.argmax(), res2.shape)
#
#         # if resIndex[0] > 5:
#         # elif resIndex[0] > 4:
#         # elif resIndex[0] > 3:
#         # elif resIndex[0] > 1:
#         # elif resIndex[0] > 0:
#         # elif resIndex[0] == 0:
#         # else:
#
#         if resIndex[0] > 5 and resIndex[1] < 2:
#             plt.scatter(resIndex[0], resIndex[1], c='cyan')
#         elif resIndex[0] > 4 and resIndex[1] < 3:
#             plt.scatter(resIndex[0], resIndex[1], c='blue')
#         elif resIndex[0] > 3 and resIndex[1] < 4:
#             plt.scatter(resIndex[0], resIndex[1], c='magenta')
#         elif resIndex[0] > 1 and resIndex[1] < 6:
#             plt.scatter(resIndex[0], resIndex[1], c='yellow')
#         elif resIndex[0] > 0 and resIndex[1] < 8:
#             plt.scatter(resIndex[0], resIndex[1], c='orange')
#         elif resIndex[0] == 0 and resIndex[1] < 10:
#             plt.scatter(resIndex[0], resIndex[1], c='red')
#
# def getY(index):
#     pass
#     # if resIndex[0] > 5:
#     # elif resIndex[0] > 4:
#     # elif resIndex[0] > 3:
#     # elif resIndex[0] > 1:
#     # elif resIndex[0] > 0:
#     # elif resIndex[0] == 0:
#     # else:
#
# def draw1():
#     for i in points:
#         res2 = som.activation_response([i])
#         resIndex = np.unravel_index(res2.argmax(), res2.shape)
#         if i[1] > 20:
#             if i[0] > 20:
#                 plt.scatter(resIndex[0], resIndex[1], c='magenta')
#             else:
#                 plt.scatter(resIndex[0], resIndex[1], c='red')
#         elif i[0] > 10:
#             if i[1] > 10:
#                 plt.scatter(resIndex[0], resIndex[1], c='yellow')
#             else:
#                 plt.scatter(resIndex[0], resIndex[1], c='orange')
#         else:
#             if i[0] > 10:
#                 plt.scatter(resIndex[0], resIndex[1], c='blue')
#             else:
#                 plt.scatter(resIndex[0], resIndex[1], c='cyan')
#
# def feature_scale(matrix):
#     X = matrix[:,0]
#     Y = matrix[:,1]
#
#     nom_x = X - X.min()
#     denom_x = X.max() - X.min()
#     # denom_x[denom_x==0] = 1
#     denom_x = 1 if denom_x == 0 else denom_x
#
#     nom_y = Y - Y.min()
#     denom_y = Y.max() - Y.min()
#     # denom_y==0 ?: 1
#     denom_y = 1 if denom_y == 0 else denom_y
#
#     return [nom_x/denom_x, nom_y/denom_y]
#
# my_scaled = feature_scale(points)
# sk_scaled = prep.normalize(points)
# # ========


# draw1()
#
# res2 = som.activation_response([[7, 10]])
# resIndex= np.unravel_index(res2.argmax(), res2.shape)
# plt.scatter(resIndex[0], resIndex[1], c='black')
# plt.tight_layout()
# plt.show()

# #==========
# # Amount of values to be tested for K
# Ks = range(2, 10)
#
# # List to hold on the metrics for each value of K
# results = []
#
# # Executing the loop
# for K in Ks:
#     model = KMeans(n_clusters=K)
#     model.fit(activation_indices)
#
#     results.append(model.inertia_)
#
# # Plotting the final result
# plt.plot(Ks, results, 'o-')
# plt.xlabel("Values of K")
# plt.ylabel("SSE")
# plt.show()
# #==========

activation_indices = []

for p in points:
    activation = som.activation_response([p])
    index = np.unravel_index(activation.argmax(), activation.shape)
    activation_indices.append(np.array(index))

from sklearn.cluster import KMeans
# Kmean = KMeans(n_clusters=3)
# Kmean.fit(activation_indices)

# #==========
# with open('kmean.pkl', 'wb') as picklerKmean:
#     pickle.dump(Kmean, picklerKmean)
#
with open('kmean.pkl', 'rb') as picklerKmean:
    Kmean = pickle.load(picklerKmean)


activation_indices = np.array(activation_indices)

# plt.scatter(activation_indices[:, 0], activation_indices[:, 1], s=50, c='b')
# plt.scatter(Kmean.cluster_centers_[0,0], Kmean.cluster_centers_[0,1], s=100, c='r', marker='s')
# plt.scatter(Kmean.cluster_centers_[1,0], Kmean.cluster_centers_[1,1], s=100, c='g', marker='s')
# plt.scatter(Kmean.cluster_centers_[2,0], Kmean.cluster_centers_[2,1], s=100, c='orange', marker='s')
# plt.scatter(Kmean.cluster_centers_[3,0], Kmean.cluster_centers_[3,1], s=100, c='yellow', marker='s')

res2 = som.activation_response([[4, 40]])
resIndex= np.unravel_index(res2.argmax(), res2.shape)
# plt.scatter(resIndex[0], resIndex[1], s=50, c='black')
print(Kmean.predict([resIndex]))
# plt.show()