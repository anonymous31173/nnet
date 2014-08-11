import idx2numpy
import numpy as np
import Autoencoder as ae
import matplotlib.pyplot as plt

# define the paths
train_img_path = '/home/avasbr/datasets/MNIST/train-images.idx3-ubyte'

# convert the raw images into feature vectors
num_img = 10000
train_img = idx2numpy.convert_from_file(train_img_path)
dummy,row,col = train_img.shape
d = row*col # dimensions
X_tr = np.reshape(train_img[:num_img],(num_img,d)).T/255. # train data matrix

# Neural network initialization parameters
n_hid = 196
decay = 0.003
beta = 3
rho = 0.1
n_iter = 400
method = 'L-BFGS'

print 'Sparse Autoencoder on MNIST data'
print '--------------------------------'
print 'Input feature size = ',d
print 'Number of hidden units: ',n_hid
print 'Optimization method: ',method

print 'Fitting a sparse autoencoder...'
# softmax regression if we don't provide hidden units
nnet = ae.Autoencoder(d=d,n_hid=n_hid,decay=decay,rho=rho,beta=beta) 
nnet.set_weights('alt_random')
nnet.fit(X_tr,method=method,n_iter=n_iter)
X_max = nnet.compute_max_activations()

def visualize_image_bases(X_max,n_hid,w=28,h=28):
	plt.figure()
	for i in range(n_hid):
		plt.subplot(14,14,i)
		curr_img = X_max[:,i].reshape(w,h)
		plt.imshow(curr_img,cmap='gray',interpolation='none')

visualize_image_bases(X_max, n_hid)
plt.show()