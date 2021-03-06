'''
	Discriminator definition for AdvGAN

	ref: https://arxiv.org/pdf/1801.02610.pdf
'''

import tensorflow as tf

def discriminator(x):
	with tf.variable_scope('d_weights', reuse=tf.AUTO_REUSE):
		input_layer = tf.reshape(x, [-1, 28, 28, 1])

		conv1 = tf.layers.conv2d(
							inputs=input_layer,
							filters=8,
							kernel_size=4,
							strides=2,
							padding="same",
							activation=None)
		conv1 = tf.nn.leaky_relu(conv1, alpha=0.2)

		
		conv2 = tf.layers.conv2d(
							inputs=conv1,
							filters=16,
							kernel_size=4,
							strides=2,
							padding="same",
							activation=None)

		in1 = tf.contrib.layers.instance_norm(conv2)
		conv2 = tf.nn.leaky_relu(in1, alpha=0.2)


		conv3 = tf.layers.conv2d(
							inputs=conv2,
							filters=32,
							kernel_size=4,
							strides=2,
							padding="same",
							activation=None)

		in2 = tf.contrib.layers.instance_norm(conv3)
		conv3 = tf.nn.leaky_relu(in2, alpha=0.2)

		in2_flatten = tf.contrib.layers.flatten(conv3)

		logits = tf.layers.dense(inputs=in2_flatten, units=1, activation=None)

		probs = tf.nn.sigmoid(logits)

		return logits, probs






