# RNN LSTM 循环神经网络分类

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# this is data
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)

# hyper-parameters
lr = 0.001
training_iters = 100000
batch_size = 128 # 一批128张图片
# display_step = 10

n_inputs = 28 # MNIST data input (ima shape:28x28)，每次input一行的28个像素
n_steps = 28 # time steps，分28次input图的28行
n_hidden_units = 128 # neurons in hidden layer
n_classes = 10 # MNIST classes (0-9)

# tf Graph input
x = tf.placeholder(tf.float32,[None,n_steps,n_inputs])
y = tf.placeholder(tf.float32,[None,n_classes])

# Define weights(采用随机初始化)
weights = {
    # (28,128)
    'in': tf.Variable(tf.random.normal([n_inputs,n_hidden_units])),
    # (128,10)
    'out': tf.Variable(tf.random.normal([n_hidden_units,n_classes]))
}
biases = {
    # (128,)
    'in': tf.Variable(tf.constant(0,1,shape=[n_hidden_units,])),
    # (10,)
    'out': tf.Variable(tf.constant(0.1,shape=[n_classes,]))
}

def RNN(X,weights,biases):
    ## hidden layer for input to cell
    # X(128 batch, 28 steps, 28 inputs) => (128*28, 28 inputs)
    X = tf.reshape(X,[-1,n_inputs])
    # => (128batch*28steps, 128 hidden)
    X_in = tf.matmul(X,weights['in'])+biases['in']
    # => (128batch, 28 steps, 128 hidden)
    X_in = tf.reshape(X_in,[-1,n_steps,n_hidden_units])
    
    ## cell
    lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden_units,forget_bias=1.0,state_is_tuple=True) # 初始定义不忘记前面的记忆
    # lstm cell is divided into two parts (c_state,m_state)
    _init_state = lstm_cell.zero_state(batch_size,dtype=tf.float32)

    outputs,states = tf.nn.dynamic_rnn(lstm_cell,X_in,initial_state=_init_state,time_major=False) # dynamic_rnn()优点在于对尺度不同的数据处理上减少计算量，time_major=False表示time不在第一维度
    
    ## hidden layer for output as the final results
    results = tf.matmul(states[1],weights['out']) + biases['out']
    # or use outputs[-1] as follows: (outputs[-1]=states[1])
    # outputs = tf.unstack(tf.transpose(outputs, [1,0,2]))
    # results = tf.matmul(outputs[-1], weights['out']) + biases['out']
    return results

pred = RNN(x,weights,biases)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred,labels=y))
train_op = tf.train.AdamOptimizer(lr).minimize(cost)

correct_pred = tf.equal(tf.argmax(pred,1),tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred,tf.float32))

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    step = 0
    while step*batch_size<training_iters:
        batch_xs,batch_ys = mnist.train.next_batch(batch_size)
        # 把数据进行批标准化，变成x批，y行，z列的数据
        batch_xs = batch_xs.reshape([batch_size,n_steps,n_inputs])
        sess.run([train_op],feed_dict={x:batch_xs,y:batch_ys})
        if step%20 == 0: # 每20次打印一次精度
            print(sess.run(accuracy,feed_dict={x:batch_xs,y:batch_ys}))
        step += 1