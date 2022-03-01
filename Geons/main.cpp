/**
 * @file main.cpp
 * @author Aswath Muthuselvam (aswath@umd.edu)
 * @brief Main File for Optical Flow
 * @version 1
 * @date 28th Feb, 2022
 * @copyright BSD3 Copyright (c) 2021
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED 
 * TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A 
 * PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT 
 * HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
 *  TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR 
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF 
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING 
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 */

#include <iostream>
#include <opencv2/opencv.hpp>
#include <unistd.h>
#include <Eigen/Core>
#include <Eigen/LU>
#include "primitive.hpp"

using namespace cv;
using namespace std;
using Eigen::Vector3d;
using Eigen::VectorXd;
using Eigen::RowVectorXd;
using Eigen::MatrixXd;
using Eigen::Matrix;

std::string GetCurrentWorkingDir();
RNG rng(1);

int main(){

    VideoCapture capture;
    Mat frame;
    vector<double> A_vec;
    vector<double> b_vec;

    std::string path = GetCurrentWorkingDir();
    Mat image = imread(path+"/../primitives.jpeg");
    Mat gray_image;

    cv::cvtColor(image, gray_image, cv::COLOR_BGR2GRAY);

    Mat binary_image;
    cv::threshold(gray_image, binary_image, 100, 120, cv::THRESH_BINARY_INV);
    imshow("Image", binary_image);

    vector<vector<cv::Point>> contours;
    vector<Vec4i> hierarchy;
    cv::findContours(binary_image, contours, hierarchy, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);
    
    Mat drawing = Mat::zeros( binary_image.size(), CV_8UC3 );
    for( size_t i = 0; i< contours.size(); i++ )
    {
        Scalar color = Scalar( rng.uniform(0, 256), rng.uniform(0,256), rng.uniform(0,256) );
        drawContours( drawing, contours, (int)i, color, 2, LINE_8, hierarchy, 0 );
    }
    imshow( "Contours", drawing );

    waitKey(5000);


    return 0;
}

std::string GetCurrentWorkingDir()
{
    std::string cwd("\0",FILENAME_MAX+1);
    return getcwd(&cwd[0],cwd.capacity());
}