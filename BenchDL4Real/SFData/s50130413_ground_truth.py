import tensorflow.compat.v1 as tf
tf.compat.v1.disable_eager_execution()

w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,3],stddev=1,seed=1))

x = tf.constant([0.7,0.9])

x = tf.expand_dims(x, 0)
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

sess = tf.Session()

sess.run(w1.initializer)
sess.run(w2.initializer)

print(sess.run(y))
sess.close()