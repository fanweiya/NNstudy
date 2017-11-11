import tensorflow as tf
import numpy as np
#creat data
x_data=np.random.rand(100).astype(np.float32)
y_data=x_data*0.1+0.3
#creat tesorflow
Weights=tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases=tf.Variable(tf.zeros([1]))
y=Weights*y_data+biases
#loss
loss = tf.reduce_mean(tf.square(y-y_data))
#gradient descent optimizer
optimizer = tf.train.GradientDescentOptimizer(0.5) #0.5 learn rate
train = optimizer.minimize(loss)
#init all var
init= tf.initialize_all_variables()
#let live
sess=tf.Session() #very important
sess.run(init)
#train
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step,sess.run(Weights),sess.run(biases),sess.run(loss))

