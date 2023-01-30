# Conan Qt5 example

```
conan new qt5Example/0.0.1 --template=cmake_exe
```

## Steps to create a conan package with gcc8 profile

```
docker run --rm -ti -v ${PWD}:/home/conan/project conanio/gcc8-ubuntu18.04
cd project

conan create . --profile:build .conan/profiles/gcc8 --profile:host .conan/profiles/gcc8 --build missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True
```

## Steps to create a conan package with cross compilation

```
docker run --rm -ti -v ${PWD}:/home/conan/project conanio/gcc8-ubuntu18.04
sudo apt -y update && sudo apt install -y crossbuild-essential-armhf
cd project

conan create . --profile:build .conan/profiles/gcc8 --profile:host .conan/profiles/linux-armv7hf-gcc7 --build missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True
```
