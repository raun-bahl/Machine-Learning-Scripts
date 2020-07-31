import numpy as np 
import math
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab


# from sklearn import svm


original_X, X_shapes = make_blobs(100,2, centers = 4, clusters_std = 1.3)
print(original_X.shape)
plt.plot(original_X[:,0], original_X[:,1], 'bo', markersize = 10)


def euclid_distance(x, xi):
	return np.sqrt(np.sum((x-xi)**2))

def neighbourhood_points(X, x_centroid, distance  = 5):
	eligible_X = []
	for x in X:
		distance_between = euclid_distance(x,x_centroid)

		if distance_between <= distance:
			eligible_X.append(x)
	return eligible_X

def gaussian_kernel(distance, bandwidth):
	val = (1/(bandwidth*math.sqrt(2*math.pi))) *\
	 np.exp(-0.5*((distance/bandwidth))**2)
	return val

X = np.copy(original_X)

past_X = []
n_iterations = 5

for it in range(n_iterations):
	for i, x in enumerate(X):

		neighbours = neighbourhood_points(X,x,look_distance)

		numerator = 0
		denominator = 0

		for neighbour in neighbours:

			distance = euclid_distance(neighbour,x)
			weight = gaussian_kernel(distance, kernel_bandwidth)
			numerator += (weight*neighbour)
			denominator += weight

		new_x = numerator/denominator

		X[i] = new_x

	past_X.append(np.copy(X))