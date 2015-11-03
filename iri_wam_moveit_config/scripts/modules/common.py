#!/usr/bin/env python

import sys 
import csv 
import tf 
import math 
import time 
import numpy 
import rospy
import shape_msgs
import moveit_commander
import moveit_msgs.msg
import moveit_msgs.srv
import dynamic_reconfigure.client

DEBUG = True

def plan_and_move_in_joints(group, jm_request):
  group.clear_pose_targets()
  if DEBUG:
    print "======= Current Joint values: %s" % group.get_current_joint_values()
    print "======= Requested Joint values: %s" % jm_request.positions
    sys.stdout.flush()
  group.set_joint_value_target(jm_request.positions)
  plan = group.plan()
  if plan.joint_trajectory.points:
    print "======= Executing trajectory plan..."
    sys.stdout.flush()
    group.go(wait=True)
    return True
  else:
    print "======= Planning NOT Possible"
    sys.stdout.flush()
    return False

def plan_and_move_in_cartesians(group, pose_st):
  group.clear_pose_targets()
  if DEBUG:
    print "======= From frame: %s" % group.get_planning_frame()
    print "======= To frame: %s" % group.get_end_effector_link()
  print "======= Generating plan"
  sys.stdout.flush()
  group.set_pose_target(pose_st)
  plan = group.plan()
  if plan.joint_trajectory.points:
    print "======= Executing plan"
    sys.stdout.flush()
    #group.go(wait=True)
    group.execute(plan)
    #wait_in_secs(2)
    print "======= Plan Executed"
    return True
  else:
    print "======= Plan NOT Possible"
    sys.stdout.flush()
    return False

