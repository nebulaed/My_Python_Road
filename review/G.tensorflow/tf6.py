# Tensorboard 可视化

import tensorflow as tf

def add_layer(inputs,in_size,out_size,activation_function=None):
    # add one more layer and return the output of this layer
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size,out_size])) # 定义权重，随机初始化比全零初始化要好很多，in_size行，out_size列
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1,out_size])+0.1) # 定义偏置，不为零初始化，1行，1行，out_size列
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs

# define placeholder for inputs to network
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32,[None,1],name='x_input') # None表示任意行，1表示1列
    ys = tf.placeholder(tf.float32,[None,1],name='y_input')

# add hidden layer
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu) # 输入为xs，insize为1,outsize为10即隐层有10个神经元，激活函数为relu函数

# add output layer
prediction = add_layer(l1,10,1,activation_function=None) # 输出层，输入为l1，inputsize=10，outsize=1，无激活函数
# 这是一个输入层神经元为1，隐层神经元为10，输出层神经元为1的神经网络

# the error between prediction and real data
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
        reduction_indices=[1])) # 利用reduce_sum求和，reduce_mean求平均值

with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
# 学习率为0.1，最小化loss

init = tf.global_variables_initializer()
sess = tf.Session()
writer = tf.summary.FileWriter("logs/",sess.graph) # 原为summary
sess.run(init) # 先运行初始化
