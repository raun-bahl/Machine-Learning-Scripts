from sklearn.decomposition import PCA
import scipy.io as sio
import matplotlib.pyplot as plot
import numpy as np

def calculate_PCA(inputSet, totalPCA):
    mu = np.mean(inputSet, axis=0)
    centerSet = inputSet - mu
    # Covariance
    covariance = np.cov(
        np.transpose(
            centerSet
        ),
        ddof=1
    )
    # w is the eigen value and v is the eigen vector
    w, v = np.linalg.eig(covariance)
    # using argsort to indices
    indices = np.argsort(np.abs(w))[::-1]
    # Applying indices on eigven value and eigen vector
    eigenVal = w[indices]
    eigenVec = v[indices]
    
    appendArray = []
    eigenArray = []
    # Selecting only first n elements for PCA elements=n
    for index in range(totalPCA):
        appendArray.append(
            eigenVec[:, indices[index]]
        )
        eigenArray.append(eigenVal[indices[index]])
    
    filteredVector = np.transpose(np.asarray(appendArray))
    value = centerSet @ filteredVector
    
    return value, eigenArray, w

data = sio.loadmat('cifar10_data_batch_1.mat')
inputSet = data['data']
labels = data['labels']

new_labels = np.isin(labels, [1, 3, 5]).flatten()

values = calculate_PCA(inputSet[new_labels], 2)

dim_reduced = values[0]
print(dim_reduced)
plot.figure()
for labelz in [1,3,5]:
    index = (labels[new_labels] == labelz).flatten()
    plot.scatter(dim_reduced[index,0], dim_reduced[index,1], label = labelz)

plot.title('PCA for Class 1, Class 3 and Class 5')
plot.xlabel('PCA 2')
plot.ylabel('PCA 1')
plot.legend()
plot.show()







