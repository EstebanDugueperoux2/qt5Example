# Conan Qt5 example

```
conan new qt5Example/0.0.1 --template=cmake_exe

docker run --rm -ti -v ${PWD}:/home/conan/project conanio/gcc8-ubuntu18.04
cd project

conan install . --build missing --profile:build .conan/profiles/gcc8 --profile:host .conan/profiles/gcc8 -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True
conan create . --profile .conan/profiles/gcc8 --build missing  -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True

```