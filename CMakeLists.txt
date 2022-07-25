cmake_minimum_required(VERSION 3.15)
project(qt5Example CXX)

find_package(Qt5 REQUIRED COMPONENTS Core)

add_executable(qt5Example src/qt5Example.cpp src/main.cpp)
target_include_directories(qt5Example PUBLIC include)

target_link_libraries(qt5Example PUBLIC Qt5::Core)

install(TARGETS qt5Example)
