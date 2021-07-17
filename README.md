# AI_TASK5_SMART_METHODS-
This work is for my second task in the AI route at [Smart Methods'](https://s-m.com.sa/c12_in.php) training program.

## Task description 
Write a Python Script that publishes to /move_base_simple/goal topic

## Task Steps

1- Creating a package:
- Open a new terminal
- First we go to where we will make our package, in the catkin Workspace
`cd ~/catkin_ws/src`

- We make a package named "custom_package" using catkin_create_pkg
`catkin_create_pkg custom_package std_msgs rospy roscpp`

2- Writing the python script and making it executable:
- first we make file in custom_package src folder. we will use the code written in this repositorie then we will change the permission to make the file executable.

```
cd ~/catkin_ws/src/custom_package/src/
wget https://raw.githubusercontent.com/Khaled-Dahhasi/AI_TASK5_SMART_METHODS-/main/goHome.py
chmod +x goHome.py
```
3- running the node:
we now have the code ready and executable. we just need to run roscore and the simulation and observe the /move_base_simple/goal topic to verify that our code works.

-open 3 terminals

-in terminal 1:
`roscore`

-in terminal 2 (observing the topic):
`rostopic echo /move_base_simple/goal`

-in terminal 3 (Run the node):
``rosrun custom_package goHome.py``

Now see how the topic got the published information to move the robot to a new location we called home.
if gazepo or RViz are opened we can see the robot moving in real time. 
