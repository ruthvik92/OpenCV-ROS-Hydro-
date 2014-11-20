#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <sstream>
#include<iostream>
using namespace cv;
using namespace std;
int main( )
{
 
for(int i=1;i<=46;i++)
{
 stringstream ss;           
 ss<<i;                      
 string si = "/home/iiith/Desktop/charminar/" + ss.str() + ".jpg"; ///jus change the path of your source ".jpg files///
 cout <<" iteration value is:"<<ss.str()<<endl;
Mat gray_image;
Mat image; 
image = imread(si,1);
if( !image.data )
 {
   printf( " No image data \n " );
   printf("i:",i);
   return -1;
 }       
cvtColor( image, gray_image, CV_BGR2GRAY );
string ssave1 = "/home/iiith/Desktop/new_charminar/" + ss.str()+ ".pgm"; ///jus change the path of your destination ".pgm" files///
imwrite( ssave1, gray_image );
 namedWindow( "jpg", CV_WINDOW_AUTOSIZE );
 namedWindow( "pgm", CV_WINDOW_AUTOSIZE );

 imshow( "jpg", image );
 imshow( "pgm", gray_image );

 waitKey(100000);
}
 return 0;
}
