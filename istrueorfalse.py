#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 15:39:52 2018

@author: ljk
"""

import matplotlib.pyplot as plt
from gen_captcha import gen_captcha_text_and_image
from yanzma import *
import numpy as np
import tensorflow as tf
def crack_captcha():
    #tf.reset_default_graph()#avoid variable change 
    output = crack_captcha_cnn()
    saver = tf.train.Saver()
    with tf.Session() as sess:
        saver.restore(sess, tf.train.latest_checkpoint('saveyzm'))
        for intt in range(10):
            text1, image = gen_captcha_text_and_image()
            plt.imshow(image)
            plt.show()
            image = convert2gray(image)
            captcha_image = image.flatten() / 255
            predict = tf.argmax(tf.reshape(output, [-1, MAX_CAPTCHA, CHAR_SET_LEN]), 2)
            text_list = sess.run(predict, feed_dict={X: [captcha_image], keep_prob: 1})
            text = text_list[0].tolist()
            vector = np.zeros(MAX_CAPTCHA*CHAR_SET_LEN)
            i = 0
            for n in text:
                vector[i*CHAR_SET_LEN + n] = 1
                i += 1
            print("正确: {}  预测: {}".format(text1, vec2text(vector)))
crack_captcha()