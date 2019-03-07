import tensorflow as tf
import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print(tf.__version__)
a = tf.constant(50.0, name="a")
b = tf.constant(5.5, name="b")
x = tf.add(a, b)
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print("%f" % sess.run(x))

add = tf.add(a, b)
mul = tf.multiply(a, b)
print("Addition with variables: %i" % sess.run(add, feed_dict={a: 2, b: 3}))
print("Multiplication with variables: %i" % sess.run(mul, feed_dict={a: 2, b: 3}))
sess.close()
print(a)
