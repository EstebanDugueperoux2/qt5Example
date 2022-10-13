# Conan Qt5 example

```
conan new qt5Example/0.0.1 --template=cmake_exe

docker run --rm -ti -v ${PWD}:/home/conan/project conanio/gcc7
cd project
export CONAN_SYSREQUIRES_MODE=enabled
conan create . --profile .conan/profiles/gcc7 --build missing  -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True

conan create . --profile .conan/profiles/gcc8 --build missing  -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True

```