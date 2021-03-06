#####################################################
########## Welcome to TensorFlow World ##############
#####################################################

# The tutorials in this section is just a start for going into TensorFlow world.
# The TensorFlow flags are used for having a more user friendly environment.

from __future__ import print_function
import tensorflow as tf
import os


######################################
######### Necessary Flags ############
# ####################################

# The default path for saving event files is the same folder of this python file.
tf.app.flags.DEFINE_string(
    'log_dir', os.path.dirname(os.path.abspath(__file__)) + '/logs',
    'Directory where event logs are written to.')

# Store all elemnts in FLAG structure!
FLAGS = tf.app.flags.FLAGS

################################################
################# handling errors!##############
################################################

# The user is prompted to input an absolute path.
# os.path.expanduser is leveraged to transform '~' sign to the corresponding path indicator.
#       Example: '~/logs' equals to '/home/username/logs'
if not os.path.isabs(os.path.expanduser(FLAGS.log_dir)):
    raise ValueError('You must assign absolute path for --log_dir')


# Defining some sentence!
welcome = tf.constant('Welcome to TensorFlow world!')

# Run the session
with tf.Session() as sess:
    writer = tf.summary.FileWriter(os.path.expanduser(FLAGS.log_dir), sess.graph)
    print("output: ", sess.run(welcome))

# Closing the writer.
writer.close()
sess.close()


