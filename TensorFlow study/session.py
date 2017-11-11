import tensorflow as tf
import numpy as np
matrix1=tf.constant([[3,3]])
matrix2=tf.constant([[2],[2]])
product=tf.matmul(matrix1,matrix2)# matrix1 .* matrix2
print(product)
#method 1
sess=tf.Session()
result=sess.run(product)
print(result)
sess.close()

#method 2
with tf.Session() as sess: #auto close session
    result2=sess.run(product)
    print(result2)
