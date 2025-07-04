import tensorflow.compat.v1 as tf
tf.compat.v1.disable_eager_execution()

batch_size = 32
chrvocabsize = 100
char_hidden_size = 64
char_num_steps = 10

# Create the cells
with tf.variable_scope('forward'):
    char_gru_cell_fw = tf.nn.rnn_cell.GRUCell(char_hidden_size)
with tf.variable_scope('backward'):
    char_gru_cell_bw = tf.nn.rnn_cell.GRUCell(char_hidden_size)

# Set initial state of the cells to be zero
_char_initial_state_fw = \
    char_gru_cell_fw.zero_state(batch_size, tf.float32)
_char_initial_state_bw = \
    char_gru_cell_bw.zero_state(batch_size, tf.float32)

chargruinput = tf.Variable(tf.random_normal(shape=[batch_size, char_num_steps, chrvocabsize]),dtype=tf.float32)
char_num_steps = [char_num_steps]*batch_size

# doc:
# sequence_length: (optional) An int32/int64 vector, size [batch_size], containing the actual
# lengths for each of the sequences in the batch. If not provided, all batch entries are assumed
# to be full sequences; and time reversal is applied from time 0 to max_time for each sequence.
# Run the bidirectional rnn and get the corner results
output_state_fw, output_state_bw = \
   tf.nn.bidirectional_dynamic_rnn(char_gru_cell_fw,
                    char_gru_cell_bw,
                    inputs=chargruinput,
                    sequence_length=char_num_steps,
                    initial_state_fw=_char_initial_state_fw,
                    initial_state_bw=_char_initial_state_bw)