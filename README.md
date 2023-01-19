# Conan Qt5 example

```
conan new qt5Example/0.0.1 --template=cmake_exe

docker run --rm -ti -v ${PWD}:/home/conan/project conanio/gcc8-ubuntu16.04
cd project

conan create . --profile:build .conan/profiles/gcc8 --profile:host .conan/profiles/gcc8 --build missing  -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True

cd inner/qt5ExampleConsumer
conan install . --build missing --profile:build ../../.conan/profiles/gcc8 --profile:host ../../.conan/profiles/gcc8 -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True

<!-- conan create . --profile:build ../../.conan/profiles/gcc8 --profile:host ../../.conan/profiles/gcc8 --build missing  -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True -->
```