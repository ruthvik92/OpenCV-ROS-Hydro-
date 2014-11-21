#!/usr/bin/env python
import roslib
import rospy
import time
from nav_msgs.msg import Odometry 
import math
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import Twist
X=-89.7505
Y=-908.127
q1=-89.7505
q2=-908.127
check = 0
def gpscapture_callback_mover(data):
    global X
    global Y 
    global q1
    global q2
    global check
    q1=data.pose.pose.position.x
    q2=data.pose.pose.position.y
    x = (X - q1)
    y = (Y - q2)  
    #print "Y is",Y         
    a=math.sqrt(x*x+y*y)
    #print "X is ",X
    #print "Y is", Y
    #print "q1 is",q1
    #print "q2 is",q2
    print "a is",a
    if a>=7:
        X=q1
        Y=q2
	check = 1 #condition setting for fetching gps data 

def gps_callback(data): #function to fetch gps 
    global check
    if check:
        lati= data.latitude
        longi=data.longitude
        print "latitude = ",lati
        f= open('/home/iiith/Desktop/gps.txt', 'a')
        f.write(("%s  %s\n" % (str(lati), str(longi))))
        f.close()
	check = 0
def position():      
    rospy.init_node('test', anonymous=True)  #initialize the node"
    rospy.Subscriber("encoder", Odometry, gpscapture_callback_mover)
    rospy.Subscriber("fix", NavSatFix, gps_callback)   
       
if __name__ == '__main__':

    try:
        position()
        rospy.spin()
    except rospy.ROSInterruptException: pass
####/// extracts GPS data for every 7 meteres///#### 







