# 添加层 def add_layer()，建造神经网络 build a neural network，结果可视化 matplotlib可视化

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size])) # 定义权重，随机初始化比全零初始化要好很多，in_size行，out_size列
    biases = tf.Variable(tf.zeros([1,out_size])+0.1) # 定义偏置，不为零初始化，1行，1行，out_size列，在机器学习中biases推荐值不为0
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

x_data = np.linspace(-1,1,300)[:,np.newaxis] # 制造一个数据，加一维度变为1列300行
noise = np.random.normal(0,0.05,x_data.shape) # 制造噪声，模拟真实数据，方差为0.05
y_data = np.square(x_data) - 0.5 + noise

xs = tf.placeholder(tf.float32,[None,1]) # None表示任意行，1表示1列
ys = tf.placeholder(tf.float32,[None,1]) # 必须用tf.float32定义数据形式
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu) # 输入为xs，insize为1,outsize为10即隐层有10个神经元，激活函数为relu函数
prediction = add_layer(l1, 10, 1, activation_function=None) # 输出层，输入为l1，inputsize=10，outsize=1，无激活函数
# 这是一个输入层神经元为1，隐层神经元为10，输出层神经元为1的神经网络

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
        reduction_indices=[1])) # 利用reduce_sum求和，reduce_mean求平均值
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
# 学习率为0.1，最小化loss

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # 先运行初始化

fig = plt.figure() # 生成一个图片框
ax = fig.add_subplot(1,1,1) # 进行连续性的plot画图，1,1,1是编号
ax.scatter(x_data,y_data) # 先把真实数据用点的形式plot出来
plt.ion() # show后不暂停，保持住界面继续
plt.show()

for i in range(1000): # 训练步数为1000
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i % 50 == 0:
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
        try: # 用try方法可能会占用较多资源，可尝试采用if检测lines变量是否存在
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs:x_data})
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5) # x轴数据不变，y轴数据改为预测结果，用红色的线表示，线的宽度为5
        # ax.lines.remove(lines[0]) # 每次画新线前要抹除旧线，此处建议采用先抹除再展示
        plt.pause(0.2) # 每次plot完暂停0.1秒再继续

plt.ioff() # 将界面停在最后一个画面
plt.show()
