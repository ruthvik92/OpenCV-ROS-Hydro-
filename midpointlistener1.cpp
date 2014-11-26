#include "ros/ros.h"
#include "std_msgs/Int16.h"
#include <iostream>
#include <geometry_msgs/Twist.h>
using namespace std;
std_msgs::Int16 msg;
int a=0;
void chatterCallback(const std_msgs::Int16 msg) //this code i should be using
{
a=msg.data;
}
int main(int argc, char **argv)
{
ros::init(argc, argv, "midpointlistener");
ros::NodeHandle n;
ros::Publisher chatter_pub = n.advertise<std_msgs::Int16>("talker", 1);
ros::Subscriber sub = n.subscribe("midpoint", 1, chatterCallback);
 ros:: Publisher vel_pub = n.advertise<geometry_msgs::Twist>("cmd_vel", 1);
geometry_msgs::Twist base_cmd;

while(ros::ok())
{
ros::spinOnce();
ROS_INFO("I heard: %d", a);
base_cmd.linear.x = a/2;
vel_pub.publish(base_cmd);
}
}

