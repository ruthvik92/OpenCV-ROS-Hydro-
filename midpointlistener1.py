#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from geometry_msgs.msg import Twist
def callback(data):
    rospy.loginfo( "%d",data.data)
    a=data.data
    if a==-2:
        pub = rospy.Publisher('/husky/cmd_vel', Twist)
        twist = Twist()
        rospy.loginfo("Moving the robot left.")
        twist.angular.z =-(a/2.5)  # 
        #for i in range(1,10):
        pub.publish(twist)
            #if a==-1 or 0 or 1:
             #   twist=Twist()
              #  pub.publish(twist)
    elif a==-1:
         rospy.loginfo("Moving the robot left.")
         twist.angular.z =-(a/1.5)  # 
         #for i in range(1,6):
         pub.publish(twist)
            #if a==1 or 0 or 2:
             #   twist=Twist()
              #  pub.publish(twist)
    elif a==1:
        rospy.loginfo("Moving the robot right.")
        twist.angular.z =-(a/1.5)  # 
        #for i in range(1,6):
        pub.publish(twist)
           # if a==-1 or 0 or -2:
            #    twist=Twist()
             #   pub.publish(twist)
    elif a==2:
        rospy.loginfo("Moving the robot right.")
        twist.angular.z =-(a/2.5)  # 
        #for i in range(1,10):
        pub.publish(twist)
           # if a==1 or 0 or -1:
            #    twist=Twist()
             #   pub.publish(twist)
    elif a==0:
        rospy.loginfo("Moving the robot straight.")
        twist.linear.x =.8 #
        #for i in range(1,10): 
        pub.publish(twist)    
        
def listener():
    rospy.init_node('midpointlistener', anonymous=True)
    rospy.Subscriber("midpoint", Int16, callback)
    pub = rospy.Publisher('/husky/cmd_vel', Twist)
    twist = Twist()
    while (ros::ok())
	ospy.spin()
        
if __name__ == '__main__':
    listener()
#### this code is so slow on Husky
