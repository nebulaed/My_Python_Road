# Session会话控制
import tensorflow as tf

matrix1 = tf.constant([[3,3]]) # 一行两列
matrix2 = tf.constant([[2],[2]]) # 两行一列

product = tf.matmul(matrix1,matrix2) # matrix multiply类似于np.dot(m1,m2)

### method 1

# sess = tf.Session()
# result = sess.run(product)
# print(result)
# sess.close()

### method 2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
### 类似for循环，只在该循环内运行Session，循环结束后会自动close
