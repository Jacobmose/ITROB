#!/usr/bin/env python

from planar import Affine
from planar import Vec2

def calculateObjectPosition(x_pixel, y_pixel):

	# x_pixel offset = +5 and y_pixel offset = -5
	# this is not done and should be set somewhere

	# Robots world coordinates seen from camera frame
	x_coordinate_robot_position = 34.7
	y_coordinate_robot_position = 33.9

	# Resolution in cm per pixel
	resolution_width = 70.0/611.0
	resolution_height = 39.5/344.0	

	# Robots position seen from camera frame
	T1 = Affine.translation((x_coordinate_robot_position, y_coordinate_robot_position))

	# Robots rotating frame opposite to camera frame - degrees
	rot = Affine.rotation(180)

	# Getting robot frame
	robot_frame = T1*rot

	# Actual distance seen from camera frame
	actual_distance_width = resolution_width*x_pixel
	actual_distance_height = resolution_height*y_pixel

	# Object position seen from camera frame
	P_yx_camera_frame = Vec2(actual_distance_height, actual_distance_width)

	# Object position seen from the robot frame
	P_xyz_robot_frame = ~robot_frame*P_yx_camera_frame

	return P_xyz_robot_frame

print(calculateObjectPosition(40, 295))

























































