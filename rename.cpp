#include <stdio.h> /////code to rename jpg files in afolder
#include <opencv2/opencv.hpp>
#include <sstream>
#include<iostream>
using namespace cv;
using namespace std;
int main( )
{
for(int j=0;j<=26;j++)
{ stringstream ss1;
	ss1<<j;

for(int i=0;i<=10;i++)
{
 stringstream ss;          
 ss<<i;                      
 string si = "/home/iiith/Desktop/bundler/Dataset_side1_far/" +std::string("node_")+ss1.str()+std::string("_") + ss.str() + ".jpg"; ///jus change the path of your source ".jpg files///
 cout <<" iteration value is:"<<ss.str()<<endl;
Mat gray_image;
Mat image;
cout<<"path"<<si; 
image = imread(si,1);
if( !image.data )
 {
   printf( " No image data \n " );
   printf("i:",i);
   return -1;
 }  
 if(j<10) 
 {    
string ssave1 = "/home/iiith/Desktop/editname/" + std::string("node0")+ss1.str() +ss.str()+".jpg"; ///jus change the path of your destination ".pgm" files///
imwrite( ssave1, image );
 waitKey(100000);
}
else
{

string ssave1 = "/home/iiith/Desktop/editname/" + std::string("node")+ss1.str() +ss.str()+".jpg"; ///jus change the path of your destination ".pgm" files///
imwrite( ssave1, image );
 waitKey(100000);
}
}
}
 return 0;

}
