import tensorflow.compat.v1 as tf
tf.compat.v1.disable_eager_execution()
V = 100
embeddings = tf.Variable(tf.random_normal([V, 1]))

norm_embed = tf.sqrt(tf.reduce_sum(tf.multiply(embeddings, embeddings), 1))
comparison = tf.greater(norm_embed, tf.constant(1.))
cond_assignment = tf.assign(embeddings, tf.where(comparison, embeddings/norm_embed, embeddings))