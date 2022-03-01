#include <cmath>
class Shape {            
     protected:
          long xo, yo, area, perimeter;
     public:
          virtual void area()=0;
          virtual void parimeter()=0;
};
class Square : public Shape {
     private:
          long side;          
     public:
          Square(){      
              area=perimeter=side=0;
          }
          void area(){
              area=side*side;       
          }
          void parimeter(){
              perimeter=4*side;       
          }
};

class Rectangle : public Shape {
     private:
          long length, width;          
     public:
          Rectangle(){      
              area=perimeter=length=width=0;
          }
          void area(){
              area=length*width;       
          }
          void parimeter(){
              perimeter=2*(length+width);       
          }
};

class Circle : public Shape {
     private:
          long radius;          
     public:
          Circle(){      
              area=perimeter=radius=0;
          }
          void area(){
              area=M_PI*radius*radius;       
          }
          void parimeter(){
              perimeter=2*M_PI*(radius);       
          }
};


class Primitives{
    Shape 

}