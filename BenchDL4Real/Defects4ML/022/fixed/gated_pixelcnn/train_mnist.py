import os
from datetime import datetime
import tensorflow as tf
import tensorflow_datasets as tfds

from model import GatedPixelCNN, bits_per_dim_loss
from utils import PlotSamplesCallback

tfk = tf.keras
tfkl = tf.keras.layers
AUTOTUNE = tf.data.experimental.AUTOTUNE

# Training parameters
EPOCHS = 75
BATCH_SIZE = 64
BUFFER_SIZE = 1024  # for shuffling

# Load dataset
mnist = tfds.load('mnist')
train_ds, test_ds = mnist['train'], mnist['test']

def prepare(element):
    image = element['image']
    image = tf.cast(image, tf.float32)
    # The image is not normalized
    return image

# PixelCNN training requires target = input
def duplicate(element):
    return element, element

train_ds = (train_ds.shuffle(BUFFER_SIZE)
                    .batch(BATCH_SIZE)
                    .map(prepare, num_parallel_calls=AUTOTUNE)
                    .map(duplicate)
                    .prefetch(AUTOTUNE))

test_ds = (test_ds.batch(BATCH_SIZE)
                   .map(prepare, num_parallel_calls=AUTOTUNE)
                   .map(duplicate)
                   .prefetch(AUTOTUNE))

# Define model
strategy = tf.distribute.MirroredStrategy()
with strategy.scope():
    model = GatedPixelCNN(hidden_dim=64, n_res=6)
    model.compile(optimizer='adam', loss=bits_per_dim_loss)

# Callbacks
time = datetime.now().strftime('%Y%m%d-%H%M%S')
log_dir = os.path.join('.', 'logs', 'gatedpixelcnn', time)
tensorboard_clbk = tfk.callbacks.TensorBoard(log_dir=log_dir)
sample_clbk = PlotSamplesCallback(logdir=log_dir)
callbacks = [tensorboard_clbk, sample_clbk]

# Fit
target = model.fit(train_ds, validation_data=test_ds, epochs=EPOCHS, callbacks=callbacks)

# ///////// Added By @Mehdi
import numpy as np
import json
loss = target.history['loss']
file = open(file="fixed/result.json", mode="w")  
model_loss = np.float64(loss)
res = {"loss" : loss}
json.dump(res, file)
file.close()