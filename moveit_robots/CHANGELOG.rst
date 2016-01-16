^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package moveit_robots
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* [feat] Added Gripper construction Xacros for Baxter
  baxter.srdf.xacro is now the new "baxter.srdf" (the old one is
  left unchanged for backwards compatibility). The xacro creates the
  standard "no-gripper" Baxter srdf by default, but can enable new
  gripper collision checks if left or right_electric_gripper args are
  set to true. Also, the link used as the kinematic tip for each arm
  (<side>_tip_name) can be set at launch
  - Set the default tip name to be <side>_gripper
  - Now a default end effector sdf takes care of the default <side>_gripper
  collisions
  - Electric Gripper specific collisions use the correct finger link names
  - Fixed a move_group arg value in demo_baxter
  - Removed nefarious planning_context.launch call from move_group.launch
  which would overwrite all args from a previous move_group.launch call
* Contributors: Ian McMahon

1.0.3 (2015-11-02)
------------------
* [fix] Manually move ikfast.h from include/ to include/baxter_ikfast\_{left/right}_arm_plugin/include
* Contributors: Kei Okada

1.0.1 (2015-09-19)
------------------
* Initial binary DEB release
* Contributors: Isaac IY Saito
