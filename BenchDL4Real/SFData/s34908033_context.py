import tensorflow.compat.v1 as tf
tf.compat.v1.disable_eager_execution()
import numpy as np

data = np.array([0.1, 0.2])
x = tf.placeholder("float", shape=[2])
T1 = tf.Variable(tf.ones([2,2]))
l1 = tf.matmul(T1, x)
init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    sess.run(l1, feed_dict={x: data})