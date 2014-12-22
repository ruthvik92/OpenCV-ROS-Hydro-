#include "ros/ros.h"
#include "std_msgs/Int16.h"
#include <iostream>
#include <geometry_msgs/Twist.h>
#include <fstream>
#include<time.h>

using namespace std;
std_msgs::Int16 msg;
int a=0;
float dt=0.065293  *1000000000;
float abc;
int bcd;
float velocity;
float thetadot;

int main(int argc, char **argv)
{
ifstream velocityFile;
velocityFile.open("/home/iiith/Desktop/velocity.txt");
ifstream thetaFile;
thetaFile.open("/home/iiith/Desktop/theta.txt");
ros::init(argc, argv, "abhishek");
ros::NodeHandle n;
ros::Publisher chatter_pub = n.advertise<std_msgs::Int16>("talker", 1);
 ros:: Publisher vel_pub = n.advertise<geometry_msgs::Twist>("/husky/cmd_vel", 1);
geometry_msgs::Twist base_cmd;


while(ros::ok() && !velocityFile.eof() && !thetaFile.eof() )  //Loop will terminate when the files reach their end
{
ros::spinOnce();

//////read from velocity file  only one value
velocityFile >> velocity;
//cout<<velocity<<"velocity\n";

/////read from theta dot file  only one value
thetaFile >> thetadot;
//cout<<thetadot<<"thetadot\n";

ros::Time begin=ros::Time::now();
//cout<<"--------------\n"<<begin.nsec<<"\n--------------";
ros::Time end= ros::Time::now();
while(end.nsec-begin.nsec <= dt)  //it will run for dt time
 { 
 base_cmd.angular.z =thetadot ;    //thetadot vale file se read hue he value yaha pe ayege 'thetadot'
 base_cmd.linear.x=velocity;//velocity vale file se read hue value yaha pe ayege'linear velocity'
 vel_pub.publish(base_cmd);
end=ros::Time::now();
}
}
return 0;
}



