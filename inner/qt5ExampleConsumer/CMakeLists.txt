cmake_minimum_required(VERSION 3.15)
project(qt5ExampleConsumer CXX)

add_executable(qt5ExampleConsumer src/qt5ExampleConsumer.cpp src/main.cpp)
target_include_directories(qt5ExampleConsumer PUBLIC include)

install(TARGETS qt5ExampleConsumer)
