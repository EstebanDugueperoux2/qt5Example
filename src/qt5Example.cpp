#include <iostream>

#include <QString>
#include "qt5Example.h"

QString qt5Example(int argc, char *argv[]){
    std::cout << "Qt version: " << qVersion() << std::endl;
    return "QString";
}
