cmake_minimum_required(VERSION 3.15)
project(qt5Example CXX)


set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt5 COMPONENTS Widgets REQUIRED)

add_executable(qt5Example src/qt5Example.cpp src/main.cpp )
target_include_directories(qt5Example PUBLIC include)

target_link_libraries(qt5Example Qt5::Widgets)

get_target_property(_target_libraries Qt5::Widgets INTERFACE_LINK_LIBRARIES)
get_target_property(_target_location Qt5::Widgets LOCATION)

message("_target_libraries: ${_target_libraries}")
message("_target_location: ${_target_location}")

install(TARGETS qt5Example)
