import numpy as np

import sklearn.preprocessing as prep
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import sys
import os
def find_root_path(path):
    head, tail = os.path.split(path)
    if "fixed" in tail or "buggy" in tail:
        return path
    else:
        return find_root_path(head)


try:
    sys.path.insert(0, find_root_path(os.path.abspath(__file__)))

except:
    print("Path Error! Aborted!")
    exit(1)
from autoencoder.autoencoder_models.VariationalAutoencoder import VariationalAutoencoder

mnist = input_data.read_data_sets('MNIST_data', one_hot = True)


def minmax_scale(X_train, X_test):
    preprocessor = prep.MinMaxScaler(feature_range=(0, 1)).fit(X_train)
    X_train = preprocessor.transform(X_train)
    X_test = preprocessor.transform(X_test)
    return X_train, X_test


def get_random_block_from_data(data, batch_size):
    start_index = np.random.randint(0, len(data) - batch_size)
    return data[start_index:(start_index + batch_size)]


X_train, X_test = minmax_scale(mnist.train.images, mnist.test.images)

n_samples = int(mnist.train.num_examples)
training_epochs = 20
batch_size = 128
display_step = 1

autoencoder = VariationalAutoencoder(n_input = 784,
                                     n_hidden = 200,
                                     optimizer = tf.train.AdamOptimizer(learning_rate = 0.001))

for epoch in range(training_epochs):
    avg_cost = 0.
    total_batch = int(n_samples / batch_size)
    # Loop over all batches
    for i in range(total_batch):
        batch_xs = get_random_block_from_data(X_train, batch_size)

        # Fit training using batch data
        cost = autoencoder.partial_fit(batch_xs)
        # Compute average loss
        avg_cost += cost / n_samples * batch_size

    # Display logs per epoch step
    if epoch % display_step == 0:
        print("Epoch:", '%04d' % (epoch + 1), \
            "cost=", "{:.9f}".format(avg_cost))

total_cost = autoencoder.calc_total_cost(X_test)
print("Total cost: " + str(total_cost))

# ///////// Added By @Mehdi
import json
file = open(file="fixed/result.json", mode="w")  
model_cost = np.float64(total_cost)
res = {"cost" : model_cost}
json.dump(res, file)
file.close()
