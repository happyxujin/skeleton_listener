#!/usr/bin/env python
import roslib
roslib.load_manifest('skeleton_listener')
import rospy
import tf

rospy.init_node('skeleton_listener',anonymous=True)
listener=tf.TransformListener()
while not rospy.is_shutdown():
	try:
       		(trans,rot)=listener.lookupTransform('/openni_depth_frame','/left_hand_1',rospy.Duration())
		print "yes"
	except (tf.LookupException,tf.ConnectivityException,tf.ExtrapolationException):
        	continue

rospy.spin()


