from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy
import time
import keras
import json
import os
# fix random seed for reproducibility
numpy.random.seed(7)

# load pima indians dataset
dataset = numpy.loadtxt(os.path.dirname(os.path.realpath(__file__)) + "/pima-indians-diabetes.data", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]

# create model
model = Sequential()
model.add(Dense(12, input_dim=8))
model.add(Activation('relu'))
model.add(Dense(8))
model.add(Activation('relu'))
#model.add(Dense(120, activation='relu'))
#model.add(Dense(36, activation='relu'))
#model.add(Dense(12, activation='relu'))
model.add(Dense(1))
model.add(Activation('sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()
# Fit the model

model.fit(X, Y, epochs=150, batch_size=10)

loss, acc = model.evaluate(X, Y)
data = {
    "accuracy": "{:.2f}".format(acc),
    "loss": "{:.6f}".format(loss),
    "train_size": str(len(X)),
    "test_size": str(0)
}

json_string = json.dumps(data)
print("Info:" + json_string);

