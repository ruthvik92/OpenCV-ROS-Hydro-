#include "ros/ros.h"
#include "std_msgs/Int16.h"
#include <iostream>
using namespace std;
std_msgs::Int16 msg;
int a=0; 
void chatterCallback(const std_msgs::Int16 msg)
{
  a=msg.data;
  ROS_INFO("I heard: %d", a);
  ros::NodeHandle n;
  ros::Publisher chatter_pub = n.advertise<std_msgs::Int16>("talker", 1);
  //msg.data=a; 
  chatter_pub.publish(msg);
   
}
int main(int argc, char **argv)
{
 
  ros::init(argc, argv, "midpointlistener");
ros::NodeHandle n;
//std_msgs::Int16 msg;
       ros::Publisher chatter_pub = n.advertise<std_msgs::Int16>("talker", 1);  
  ros::Subscriber sub = n.subscribe("midpoint", 1, chatterCallback);

  while(ros::ok())
 {  	
        

      ros::spinOnce();
 //msg1=msg.data;
   //chatter_pub.publish(a);
  //msg1.data=msg.data;
       
} 

}

