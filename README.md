# AI_TASK5_SMART_METHODS-
This work is for my second task in the AI route at [Smart Methods'](https://s-m.com.sa/c12_in.php) training program.

## Task description 
Write a Python Script that publishes to /move_base_simple/goal topic

## Task Steps

1-creating a package:
- Open a new terminal
- First we go to where we will make our package, in the catkin Workspace
`cd ~/catkin_ws/src`

- We make a package named "custom_package" using catkin_create_pkg
`catkin_create_pkg custom_package std_msgs rospy roscpp`

2- Writing the python script:
- first we make file in custom_package src folder 
```
cd ~/catkin_ws/src/custom_package1/src/
touch goHome.py
```
