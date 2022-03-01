#include <cmath>
#include <Eigen/Core>
#include <Eigen/LU>
#include <vector>

using Eigen::VectorXd;
using std::vector;

class Point{
    double x,y,z;
};

class Shape {            
     protected:
          long area_, perimeter_;
     public:
          virtual void area();
          virtual void parimeter();
};
class Square : public Shape {
     private:
          long side;          
     public:
          Square(){      
              area_=perimeter_=side=0;
          }
          void area(){
              area_=side*side;       
          }
          void parimeter(){
              perimeter_=4*side;       
          }
};

class Rectangle : public Shape {
     private:
          long length, width;          
     public:
          Rectangle(){      
              area_=perimeter_=length=width=0;
          }
          void area(){
              area_=length*width;       
          }
          void parimeter(){
              perimeter_=2*(length+width);       
          }
};

class Circle : public Shape {
     private:
            long radius;          
     public:
            Circle(){      
                area_=perimeter_=radius=0;
            }
            void area(){
                area_=M_PI*radius*radius;       
            }
            void parimeter(){
                perimeter_=2*M_PI*(radius);       
            }
            void fit(vector<Point> points){
                perimeter_=2*M_PI*(radius);       
            }
};

class Primitives{
    public:
        Circle circle;
        Rectangle rectangle;
        Square sqaure;

};