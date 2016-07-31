#!/usr/bin/env python
#
# Usage:
# rosrun iri_wam_moveit_config simple_moveit_example.py
#
# Example:
# rosrun iri_wam_moveit_config simple_moveit_example.py
#
# Workaround:
#  If low level is given free memory problems, try exporting the env variable:
#    - export MALLOC_CHECK_=2
#
import roslib; roslib.load_manifest('iri_wam_moveit_config')

import sys
sys.path.append('./modules')
import getopt 
import copy
import rospy
import tf 
import time 
import numpy 
import math 
import dynamic_reconfigure.client

from subprocess                  import call
from pprint                      import pprint

from geometry_msgs.msg           import Pose, PoseStamped, PoseArray
from iri_common_drivers_msgs.srv import QueryJointsMovement, QueryJointsMovementRequest

import moveit_commander
import moveit_msgs.msg

import common

home_pose = QueryJointsMovementRequest()
home_pose.positions = [0.0,-0.4, 0.0, 2.4, 0.0, 0.5, 0.0]
home_pose.velocity = 0.5
home_pose.acceleration = 0.5
initial_pose = QueryJointsMovementRequest()
initial_pose.positions = [0.0, -0.44, 0.0, 2.25, 0.0, 0.72, 0.0]
initial_pose.velocity = 0.5
initial_pose.acceleration = 0.5

if __name__ == "__main__":

  print "======= Init Simple MoveIt Example"
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node('iri_simple_moveit_example', anonymous=True)

  print "======= Connecting Node with MoveIt"
  sys.stdout.flush()
  robot = moveit_commander.RobotCommander()
  scene = moveit_commander.PlanningSceneInterface()
  group = moveit_commander.MoveGroupCommander("arm")
  group.set_planning_time(30)
  group.set_planner_id("RRTkConfigDefault")

  # Go To Initial Pose
  common.plan_and_move_in_joints(group, initial_pose)
  # Wait 5 seconds
  time.sleep(5)
  # Define a pose in Cartesian
  pose_st = PoseStamped()
  pose_st.header.frame_id    = "iri_wam_link_base"
  pose_st.header.stamp       = rospy.Time()
  pose_st.pose.position.x    = 0.359  
  pose_st.pose.position.y    =-0.037
  pose_st.pose.position.z    = 0.386
  pose_st.pose.orientation.x = 0.648
  pose_st.pose.orientation.y =-0.633
  pose_st.pose.orientation.z = 0.259
  pose_st.pose.orientation.w =-0.335
  # Go to the Cartesian Pose
  common.plan_and_move_in_cartesians(group, pose_st)
  # Wait 5 seconds
  time.sleep(5)
  # Go To Initial Pose
  common.plan_and_move_in_joints(group, home_pose)

  print "======= THE END"
  sys.stdout.flush()
  moveit_commander.os._exit(0)
