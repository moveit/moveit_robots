cmake_minimum_required(VERSION 2.8.3)
project(baxter_moveit_config)

find_package(catkin REQUIRED)

catkin_package()

catkin_install_python(PROGRAMS scripts/dummy_joint_trajectory_controller
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
