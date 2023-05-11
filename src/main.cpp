#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    auto window1 = Examples::Window1{};
    window1.show();

    return a.exec();
}