#!/usr/bin/env python


import rospy
from geometry_msgs.msg import PoseStamped

#publisher and node constructing
pub = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=5)
rospy.init_node("GoingHome", anonymous=True)
#using a while loop with a condition so the code will stop running when the rospy node is shutdown. this makes sure ctrl+c works  
while not rospy.is_shutdown(): 
#contructing a 'home' of type PoseStamped and filling it with the info to be published 
 home=PoseStamped()
#header info
 home.header.seq=0;
 home.header.stamp=rospy.Time.now()
 home.header.frame_id="map"
#pose info
 home.pose.position.x=-1.14915668964
 home.pose.position.y=-0.526947319508
 home.pose.position.z=0.0
 home.pose.orientation.x=0.0
 home.pose.orientation.y=0.0
 home.pose.orientation.z=0.0149994446208
 home.pose.orientation.w=0.999887502003
 
# a delay so the publisher can find time to make a connection with any subscribers      
 rospy.sleep(1)

 rospy.loginfo("goal published. going home.... ID is:%d",home.header.seq)
 pub.publish(home)


   
