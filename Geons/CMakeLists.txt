cmake_minimum_required(VERSION 3.0)
project(Geons)
find_package(OpenCV)
find_package(Eigen3)

include_directories(${OpenCV_INCLUDE})

add_executable(geons main.cpp)

target_link_libraries(geons ${OpenCV_LIBS} Eigen3::Eigen)