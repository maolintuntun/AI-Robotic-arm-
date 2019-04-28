# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 16:20:27 2017

@author: YT
"""

from __future__ import print_function
import tensorflow as tf

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2],
                       [2]])
product = tf.matmul(matrix1, matrix2)  # matrix multiply np.dot(m1, m2)

# method 1
#sess = tf.Session()
#result = sess.run(product)
#print(result)
#sess.close()
#
## method 2
#with tf.Session() as sess:
#    result2 = sess.run(product)
#    print(result2)

print(product)

