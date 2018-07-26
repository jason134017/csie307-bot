# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:51:53 2018

@author: User
"""

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))