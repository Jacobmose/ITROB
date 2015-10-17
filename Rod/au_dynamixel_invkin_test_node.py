#!/usr/bin/env python


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
xy_Value = calcObjectPos.calculateObjectPosition(136,304)

# def PickupBrick(x,y):
# 	return	[[x, y, 8, 0, 0],[x, y, 1, 0.8, 0],[x, y, 8, 0.8, 0],[0, 25, 15, 0.8, 0]]
def gnaf(x11, y22):
	return [[-1, 18 ,10, 0, 0],[-1, 18 ,1, 0, 0],[0, 18 ,1, 0.8, 0],[0, 18 ,10, 0.8, 0],[25, 0, 15, 0.8, 0]]
	
 	

def invkin(xyz):
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
	def __init__(self,server_name):
		self.client = actionlib.SimpleActionClient(server_name, FollowJointTrajectoryAction)

		self.joint_positions = []
		self.names =["joint1",
				"joint2",
				"joint3",
				"joint4",
				"gripper"
				
				]
		# the list of xyz points we want to plan
		#These values are given in centimeters:   
		xyz_positions = gnaf(20,20)
###########BLOCKS PILED UP!######################################				
#		#ROED KLODS
#		
# 		[14.5, 30, 10, 0, 0], 
#  		[14.5, 30, 1, 0, 0], 
# 		[14.5, 30, 1, 0.8, 0],
#  		[14.5, 30, 10, 0.8, 0],
# 		[25, 0, 15, 0.8, 0], 		#Go to center of X (move poss.)
# 		[-3, -30.5, 15, 0.8, 0], 	#Poss above putdown poss.
# 		[-3, -30.5, 3.5, 0.8, 0], 		
# 		[-3, -30.5, 1, 0.5, 0],
# 		[-3, -30.5, 5, 0.5, 0], 	#Go a little up to avoid hitting block
#   		
#  		[25, 0, 20, 0.5, 0], 		# Go to home poss.
#  		
# 		#GROEN KLODS
#  		[-1, 18 ,10, 0, 0],
#   	[-1, 18 ,1, 0, 0],
#  		[0, 18 ,1, 0.8, 0],
# 		[0, 18 ,10, 0.8, 0],
# 		[25, 0, 15, 0.8, 0], 		#Go to center of X (move poss.)
# 		[-3, -28.8, 13, 0.8, 0], 	#Poss above putdown poss.
# 		[-3, -28.8, 13, 0.8, 0], 	#Poss above putdown poss.
#  		[-3, -28.8, 6.5, 0.8, 0], 		
#  		[-3, -28.8, 4, 0.5, 0],
#  		[-3, -28.8, 10, 0.5, 0], 	#Go a little up to avoid hitting block
#   		
#   		[25, 0, 20, 0.5, 0], 	# Go to home poss.
#   		
#  		#BLAA KLODS
# 		[21, 12.5, 10, 0, 0],
#  		[21, 12.5, 1, 0, 0],		#Z = 1 when gripper is going to block
#  		[21, 12.5, 1, 0.8, 0],		#Z = 3.5 When gripper is griping
#  		[21, 12.5, 10, 0.8, 0],
#  		[25, 0, 15, 0.8, 0], 		#Go to center of X (move poss.)
#  		[-3, -28.8, 15, 0.8, 0], 	#Poss above putdown poss.
# 		[-3, -28.8, 15, 0.8, 0], 	#Poss above putdown poss.
#  		[-3, -28.8, 8.5, 0.8, 0], 		
#  		[-3, -28.8, 5, 0.5, 0],
#  		[-3, -28.8, 12, 0.5, 0], 	#Go a little up to avoid hitting block
#  		
#  		[-3, -28.8, 8, 1.2, 0], 
#  		[-3, -28.8, 12, 1.2, 0], 
#  		[-3, -28.8, 8, 1.2, 0], 
#  		
#  		
#   	[25, 0, 20, 0.5, 0], 		# Go to home poss.

##########BLOCKS TO MARKED POINTS!######################################	
#
#		#ROED KLODS
#		
# 		[14.5, 30, 10, 0, 0], 
#  		[14.5, 30, 1, 0, 0], 
# 		[14.5, 30, 1, 0.8, 0],
#  		[14.5, 30, 10, 0.8, 0],
# 		[25, 0, 15, 0.8, 0], 		#Go to center of X (move poss.)
#  		[25, -15, 8, 0.8, 0], 	#Poss above putdown poss.
#  		[25, -15, 2, 0.8, 0], 	#Poss above putdown poss.
#  		[25, -15, 2, 0.5, 0], 	#Poss above putdown poss.
#  		[25, -15, 8, 0.5, 0], 	#Poss above putdown poss.
#    		

 		
	 	
   	
   	

#  		
# 		#GROEN KLODS
 #		[-1, 18 ,10, 0, 0],
#   	[-1, 18 ,1, 0, 0],
# 		[0, 18 ,1, 0.8, 0],
# 		[0, 18 ,10, 0.8, 0],
# 		[25, 0, 15, 0.8, 0], 		#Go to center of X (move poss.)
		#HHHHHHHHHHHHHHHHER ER DU KOMMMMMMMMMMMMMMMMET TILLLLLLLLLLLLLLLLll!!!!!!!!!!!!!!!!!!!
# 		[20, -20, 8, 0.8, 0], 	#Poss above putdown poss.
# 		[20, -20, 2, 0.8, 0], 	#Poss above putdown poss.
# 		[-3, -28.8, 13, 0.8, 0], 	#Poss above putdown poss.
#  		[-3, -28.8, 6.5, 0.8, 0], 		
#  		[-3, -28.8, 4, 0.5, 0],
#  		[-3, -28.8, 10, 0.5, 0], 	#Go a little up to avoid hitting block
#   		
 #  		[25, 0, 20, 0.8, 0], 	# Go to home poss.
#   		
#  		#BLAA KLODS
# 		[21, 12.5, 10, 0, 0],
#  		[21, 12.5, 1, 0, 0],		#Z = 1 when gripper is going to block
#  		[21, 12.5, 1, 0.8, 0],		#Z = 3.5 When gripper is griping
#  		[21, 12.5, 10, 0.8, 0],
#  		[25, 0, 15, 0.8, 0], 		#Go to center of X (move poss.)
#  		[-3, -28.8, 15, 0.8, 0], 	#Poss above putdown poss.
# 		[-3, -28.8, 15, 0.8, 0], 	#Poss above putdown poss.
#  		[-3, -28.8, 8.5, 0.8, 0], 		
#  		[-3, -28.8, 5, 0.5, 0],
#  		[-3, -28.8, 12, 0.5, 0], 	#Go a little up to avoid hitting block
#  		
#  		[-3, -28.8, 8, 1.2, 0], 
#  		[-3, -28.8, 12, 1.2, 0], 
#  		[-3, -28.8, 8, 1.2, 0], 
#  		
#  		
#   	[25, 0, 20, 0.5, 0], 		# Go to home poss.
 
###########BLOCK PICKUP TEST######################################				
		#Klods Roed
# 		[13.5, 29, 8, 0.5, 0],
# 		[13.5, 29, 1.2, 0.5, 0],
# 		[13.5, 29, 3.5, 0.75, 0],
# 		[13.5, 29, 8, 0.75, 0],
# 		[13.5, 29, 3.5, 0.5, 0],
#  
#  		[13.5, 29, 10, 0.5, 0], 		#Go a little up to avoid hitting block
#   		
#  
# 		#Klods Groen
#  		[0.5, 18.5, 8, 0.5, 0],	
#  		[0.5, 18.5, 2, 0.5, 0],
# 		[0.5, 18.5, 3.5, 0.75, 0],
# 		[0.5, 18.5, 8, 0.75, 0],
# 	
#  		[0.5, 18.5, 10, 0.5, 0], 		#Go a little up to avoid hitting block
#   				
#  
#  		#Klods Blaa
#   	[21, 12.5, 8, 0.5, 0],
#    	[21, 12.5, 1.8, 0.5, 0],	
#    	[21, 12.5, 3.5, 0.75, 0],	#Z = 3.5 When gripper is griping
#    	[21, 12.5, 8, 0.75, 0],	
#    	[21, 12.5, 3.5, 0.5, 0],
#  	
#  		[21, 12.5, 10, 0.5, 0], 		#Go a little up to avoid hitting block

###########COIN PICKUP ######################################				

##############GAMLE VAERDIER########			
#  		[0.3672, 18.319, 3, 0.5, 0], #Blaa
#  		[0.3672, 18.319, 0, 0.5, 0], 
#  		[0.3672, 18.319, 1, 0.8, 0], 
#  		
# 		[0, 0, 58.4, 0.5, 0],		# Go to home poss.
#   	[0, 0, 58.4, 0.5, 0],		# Go to home poss.
#   	 	
#  		[21.6099, 12.8198, 3, 0.2, 0], #Gul
#  		[21.6099, 12.8198, 0, 0.2, 0],
#  		[21.6099, 12.8198, 1, 0.8, 0],
#  		
# 		[0, 0, 58.4, 0.5, 0],		# Go to home poss.
#    	[0, 0, 58.4, 0.5, 0],		# Go to home poss.
#  
#  		[30.6811, -2.1884, 3, 0.2, 0], #Groen
#  		[30.6811, -2.1884, 0, 0.2, 0],
#  		[30.6811, -2.1884, 1, 0.8, 0],
#  		
#  		[0, 0, 58.4, 0.5, 0],		# Go to home poss. 


		
		

		
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
		print self.goal
		self.client.send_goal(self.goal)

		self.client.wait_for_result()
		print self.client.get_result()

if __name__ == "__main__":
	rospy.init_node("au_dynamixel_test_node")

	node= ActionExampleNode("/arm_controller/follow_joint_trajectory")

	node.send_command()
