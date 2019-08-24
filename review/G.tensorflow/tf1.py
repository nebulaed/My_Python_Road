# Tensorflow小栗子
import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1+0.3

### create tensorflow structure start ###
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0)) # 生成-1到1的一维随机数据
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5) # 梯度下降优化 学习率(0~1)为0.5
train = optimizer.minimize(loss) # 优化最小化误差

# init = tf.initialize_all_variables() 
# initialize_all_variables (from tensorflow.python.ops.variables) is deprecated and will be removed.
# Use 'tf.global_variables_initializer' instead.
init = tf.global_variables_initializer()

### create tensorflow structure end ###

sess = tf.Session()
sess.run(init) # 激活初始化

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights),sess.run(biases))
