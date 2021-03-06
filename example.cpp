#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "iostream"
 
using namespace cv;
using namespace std;
 
int main( )
{
 
    Mat src1;
    src1 = imread("/home/iiith/Desktop/1.jpg", CV_LOAD_IMAGE_COLOR); //load image.
    namedWindow( "Original image", CV_WINDOW_AUTOSIZE ); //create a window and resize automatically.
    imshow( "Original image", src1 ); // show the image.
 
    Mat gray;
    cvtColor(src1, gray, CV_BGR2GRAY); //convert src1(clolr) to gray(b&w).
    namedWindow( "Gray image", CV_WINDOW_AUTOSIZE ); 
    imshow( "Gray image", gray );
 
    // know the number of channels the image has
    cout<<"original image channels: "<<src1.channels()<<",gray image channels: "<<gray.channels()<<endl;
 
// ******************* READ the Pixel intensity *********************
    // single channel grey scale image (type 8UC1) and pixel coordinates x=5 and y=2
    // by convention, {row number = y} and {column number = x}
    // intensity.val[0] contains a value from 0 to 255
    Scalar intensity1 = gray.at<uchar>(2, 5);
    cout << "Intensity(gray image(8UC1)) = " << endl << " " << intensity1.val[0] << endl << endl;
 
    // 3 channel image with BGR color (type 8UC3)
    // the values can be stored in "int" or in "uchar". Here int is used.
    Vec3b intensity2 = src1.at<Vec3b>(10,15);   //intensity2(vec3b) stores 3 values in a array[2]
    int blue = intensity2.val[0];
    int green = intensity2.val[1];
    int red = intensity2.val[2];
    cout << "Intensity(BGR image 8UC3) = " << endl << " " << blue << " " << green << " " << red << endl << endl;
 
// ******************* WRITE to Pixel intensity **********************
    // This is an example in OpenCV 2.4.6.0 documentation
    Mat H(10, 10, CV_64F);
    for(int i = 0; i < H.rows; i++)
        for(int j = 0; j < H.cols; j++)
            H.at<double>(i,j)=1./(i+j+1);
    cout<<H<<endl<<endl;
 
    // Modify the pixels of the BGR image
    for (int i=100; i<src1.rows; i++)
    {
        for (int j=100; j<src1.cols; j++)
        {
                src1.at<Vec3b>(i,j)[0] = 200;
                src1.at<Vec3b>(i,j)[1] = 200;
                src1.at<Vec3b>(i,j)[2] = 200;           
        }
    }
    namedWindow( "Modify pixel", CV_WINDOW_AUTOSIZE ); 
    imshow( "Modify pixel", src1 );
 
    waitKey(0);                                        
    return 0;
} 
