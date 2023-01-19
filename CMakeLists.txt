cmake_minimum_required(VERSION 3.15)
project(qt5Example CXX)


set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt5 COMPONENTS Core REQUIRED)

add_library(qt5Example src/qt5Example.cpp)
target_include_directories(qt5Example PUBLIC include)

target_link_libraries(qt5Example Qt5::Core)

install(TARGETS qt5Example)
