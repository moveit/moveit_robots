#!/usr/bin/env bash

wstool set baxter_common --git https://github.com/RethinkRobotics/baxter_common.git -v kinetic-devel -y
wstool update baxter_common
cat .rosinstall
