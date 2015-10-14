#!/usr/bin/python

import time
import rospy
import actionlib
from CalculateObjectPosition import calcObjectPos
from control_msgs.msg import FollowJointTrajectoryAction
from control_msgs.msg import FollowJointTrajectoryFeedback
from control_msgs.msg import FollowJointTrajectoryResult
from control_msgs.msg import FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
from trajectory_msgs.msg import JointTrajectory
import math
yoff = 0.6

def invkin(xyz):
	print("test", xyz)
	"""
	Python implementation of the the inverse kinematics for the crustcrawler
	Input: xyz position
	Output: Angels for each joint: q1,q2,q3,q4
	
	You might adjust parameters (d1,a1,a2,d4).
	The robot model shown in rviz can be adjusted accordingly by editing au_crustcrawler_ax12.urdf
	"""

	d1 = 16.5; # cm (height of 2nd joint)
	a1 = 0.0; # (distance along "y-axis" to 2nd joint)
	a2 = 17.5; # (distance between 2nd and 3rd joints)
	d4 = 24.5; # (distance from 3rd joint to gripper center - all inclusive, ie. also 4th joint)
	
	max = 57.8
	xc = xyz[0]+yoff;
	yc = xyz[1];
	zc = xyz[2];
	gripper = xyz[3];
	Rotater = xyz[4];
	
	q1 = math.atan2(yc,xc);
	
	r2 = pow((xc - a1*math.cos(q1)),2) + pow((yc - a1*math.sin(q1)),2);
	s = (zc - d1);
	D = (r2 + pow(s,2) - pow(a2,2) - pow(d4,2))/(2*a2*d4);

	q3 = math.atan2(-math.sqrt(1-pow(D,2)), D);
	q2 = math.atan2(s, math.sqrt(r2)) - math.atan2(d4*math.sin(q3), a2 + d4*math.cos(q3));	

	return q1,-(math.pi/2-q2),q3,Rotater, gripper

class ActionExampleNode:
	N_JOINTS = 5
	def __init__(self,server_name, x_coord, y_coord, angle, isPickup):
		self.client = actionlib.SimpleActionClient(server_name, FollowJointTrajectoryAction)

		self.joint_positions = []
		self.names =["joint1",
				"joint2",
				"joint3",
				"joint4",
				"gripper"]
		
		# the list of xyz points we want to plan
		#These values are given in centimeters:  
		if isPickup:
			xyz_positions = pickup(x_coord, y_coord)
		else:
			xyz_positions = delivery(x_coord, y_coord, angle)	
		
		# initial duration
		dur = rospy.Duration(2) #Init Speed

		# construct a list of joint positions by calling invkin for each xyz point
		for p in xyz_positions:
			jtp = JointTrajectoryPoint(positions=invkin(p),velocities=[0.5]*self.N_JOINTS ,time_from_start=dur)
			dur += rospy.Duration(1.8) #speed
			self.joint_positions.append(jtp)

		self.jt = JointTrajectory(joint_names=self.names, points=self.joint_positions)
		self.goal = FollowJointTrajectoryGoal( trajectory=self.jt, goal_time_tolerance=dur+rospy.Duration(2) )

	def send_command(self):
		self.client.wait_for_server()
		#print self.goal
		self.client.send_goal(self.goal)

		self.client.wait_for_result()
		#print self.client.get_result()

class ObjectPosition(object):
	def __init__(self, y_coord=None, x_coord=None, color=None, angle=None):
		self.y_coord = y_coord
		self.x_coord = x_coord
		self.color = color
		self.angle = angle

def checkForQRCode():
	print("Sleep 2 seconds..")
	time.sleep(2)
	return 1

def getQRString():
	return "patternTest"
	#return "patternTest2"

def getPattern(QRString):
	if QRString == "patternTest":		
		patternTestList = []
		patternTestList.append(ObjectPosition(-23, 0, "red", 0))
		patternTestList.append(ObjectPosition(-24, 15, "blue", 42))
		patternTestList.append(ObjectPosition(-23.3, 10, "green", 32))	
		patternTestList.append(ObjectPosition(-23, 5, "yellow", 18))	
		return patternTestList
	elif QRString == "patternTest2":
		patternTestList = []
		patternTestList.append(ObjectPosition(-24.3, 12, "red", -65))
		patternTestList.append(ObjectPosition(-19, 13.5, "yellow", 42))
		patternTestList.append(ObjectPosition(-21, 5, "green", 20))
		patternTestList.append(ObjectPosition(-15, 8, "blue", -60))			
		return patternTestList

def getBrickPosition(color):
	if color== "red":
		return [300, 100]
		#return [248, 110]
	elif color == "green":	
		return [300, 100]	
		#return [130, 130]
	elif color == "blue":
		return [300, 100]
		#return [65, 230]
		return [300, 100]
	elif color == "yellow":
		#return [110, 272]
		return [300, 100]

def pickup(x, y):
	return [[x, y, 10, 0.2, 0],[x, y, 1, 0, 0],[x, y, 1, 0.8, 0],[x, y, 10, 0.8, 0],[25, 0, 15, 0.8, 0]]

def delivery(x, y, angle):
	motorAngleValue = angle/58.33
	return [[x, y, 10, 0.8, 0],[x, y, 10, 0.8, motorAngleValue],[x, y, 1, 0.8, motorAngleValue],[x, y, 1, 0.5, motorAngleValue],[x, y, 10, 0.5, motorAngleValue],[25, 0, 15, 0.2, 0]]
	

def main():
	rospy.init_node("au_dynamixel_test_node")
	
	while 1:	
		while checkForQRCode():
			print("QR code found")		

			QRString = getQRString()

			PatternArray = getPattern(QRString)

			for position in PatternArray:
				color = position.color
				print(color)
				pixel_coord = getBrickPosition(color)
				pickup_coord = calcObjectPos.calculateObjectPosition(pixel_coord[0], pixel_coord[1])
				print(pickup_coord[0],pickup_coord[1])
				node = ActionExampleNode("/arm_controller/follow_joint_trajectory", pickup_coord[0], pickup_coord[1], 0, 1)
				node.send_command()
				#pickup(pickup_coord[0],pickup_coord[1])
				#print(pickup_coord)
				
				node = ActionExampleNode("/arm_controller/follow_joint_trajectory", position.x_coord, position.y_coord, position.angle, 0)
				node.send_command()
				#delivery(position.x_coord, position.y_coord)
				print(position.x_coord, position.y_coord)
			break
		break


if __name__ == '__main__':
	main()


		
