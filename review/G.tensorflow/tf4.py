# Placeholder 传入值

import tensorflow as tf

input1 = tf.placeholder(tf.float32) # 可用,[]规定结构
input2 = tf.placeholder(tf.float32)

# output = tf.mul(input1,input2) # mul已被multiply取代
output = tf.multiply(input1,input2)

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[7.],input2:[2.]})) # 以字典形式输入
# 7x2