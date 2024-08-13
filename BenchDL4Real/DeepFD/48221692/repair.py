import pandas as pd
import numpy
from sklearn.preprocessing import StandardScaler
# Import the dataset
from keras import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import json
import os

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

# Import the dataset
dataset = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + "/dataset/Linear_Data.csv", header=None).values
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:, 0:1], dataset[:, 1],
                                                    test_size=0.25, )

# Now we build the model
neural_network = Sequential()  # create model
neural_network.add(Dense(5, input_dim=1, activation='sigmoid'))  # hidden layer
# fix 1: act sigmoid -> linear
neural_network.add(Dense(1, activation='linear'))  # output layer
neural_network.compile(loss='mean_squared_error', optimizer='sgd')
neural_network_fitted = neural_network.fit(X_train, Y_train, epochs=1000, verbose=1, batch_size=X_train.shape[0], initial_epoch=0)
mse = neural_network.evaluate(X_test, Y_test)

data = {
    "accuracy": "{:.2f}".format(mse),
    "loss": "{:.6f}".format(mse),
    "train_size": str(len(X_train)),
    "test_size": str(len(X_test))
}

json_string = json.dumps(data)
print("Info:" + json_string);
