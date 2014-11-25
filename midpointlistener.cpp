

/// subscriber node values published by roadmidpoint.cpp
#include "ros/ros.h"
#include "std_msgs/Int16.h"

 std_msgs::Int16 msg;
void chatterCallback(const std_msgs::Int16 msg)
{
  ROS_INFO("I heard: %d", msg.data);
}

int main(int argc, char **argv)
{
 
  ros::init(argc, argv, "midpointlistener");

 
  ros::NodeHandle n;

 
  ros::Subscriber sub = n.subscribe("midpoint", 1, chatterCallback);


  ros::spin();

  return 0;
}
