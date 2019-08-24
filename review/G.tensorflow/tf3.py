# Variable 变量

import tensorflow as tf

state = tf.Variable(0,name='counter') # 把state定义变量，初始值为0，名字是counter

# print(state.name)
one = tf.constant(1)

new_value = tf.add(state,one)
update = tf.assign(state,new_value)

init = tf.global_variables_initializer() # must have if define variable

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print (sess.run(state))
