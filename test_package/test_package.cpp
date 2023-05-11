#include <cstdlib>
#include <iostream>
#include "qt5Example.h"


int main(int argc, char *argv[]) {
    std::cout << "Create a minimal usage for the target project here." << std::endl;
    std::cout << "Avoid big examples, bigger than 100 lines" << std::endl;
    std::cout << "Avoid networking connections." << std::endl;
    std::cout << "Avoid background apps or servers." << std::endl;
    std::cout << "The propose is testing the generated artifacts only." << std::endl;

    qt5Example(argc, argv);

    return EXIT_SUCCESS;
}