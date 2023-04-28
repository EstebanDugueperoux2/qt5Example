# Conan Qt5 example

```
conan new qt5Example/0.0.1 --template=cmake_exe
```

## Steps to create a conan package with gcc8 profile

```
docker run --rm -ti -v ${PWD}:/home/conan/project conanio/gcc8-ubuntu18.04
cd project
sudo pip install --upgrade conan
conan create . --profile:build .conan/profiles/gcc8 --profile:host .conan/profiles/gcc8 --build missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True
```

## Steps to create a conan package with arm cross compilation 

```
docker run --rm -ti -v ${PWD}:/home/conan/project conanio/gcc8-ubuntu18.04
sudo apt -y update && sudo apt install -y crossbuild-essential-armhf
cd project
sudo pip install --upgrade conan
conan create . --profile:build .conan/profiles/gcc8 --profile:host .conan/profiles/linux-armv7hf-gcc7 --build missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True
```

## Steps to create a conan package with mingw cross compilation 

```
docker run --rm -ti -v ${PWD}:/home/conan/project conanio/gcc8-ubuntu18.04
sudo apt -y update && sudo apt install -y g++-mingw-w64
cd project
sudo pip install --upgrade conan
conan create . --profile:build .conan/profiles/gcc8 --profile:host .conan/profiles/mingw64 --build missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True
```
