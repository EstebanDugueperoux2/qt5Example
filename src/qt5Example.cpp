#include <iostream>

#include <QtCore>
#include <QApplication>
#include <QWidget>

#include "qt5Example.h"

int qt5Example(int argc, char *argv[]){
    std::cout << "Qt version: " << qVersion() << std::endl;

    QApplication app(argc, argv);

    QWidget window;

    window.resize(250, 150);
    window.setWindowTitle("Simple example");
    window.show();

    return app.exec();
}
