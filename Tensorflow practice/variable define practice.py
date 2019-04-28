# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:06:24 2017

@author: YT
"""



import tensorflow as tf

biases = tf.Variable(tf.zeros([1, 3]) + 0.1)
init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(biases))