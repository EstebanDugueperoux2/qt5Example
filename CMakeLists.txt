cmake_minimum_required(VERSION 3.15)
project(qt5Example CXX)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt5 COMPONENTS Core Widgets REQUIRED)

add_executable(qt5Example src/main.cpp src/mainwindow.h)

target_link_libraries(qt5Example Qt5::Widgets)

install(TARGETS qt5Example)
