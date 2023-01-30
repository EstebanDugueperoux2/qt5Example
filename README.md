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

#docker run --rm -ti -v ${PWD}:/home/conan/project conanio/gcc9-armv7hf bash
#sudo pip install --upgrade conan

conan create . --profile:build .conan/profiles/gcc8 --profile:host .conan/profiles/linux-armv7hf-gcc7 --build missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True
```

Get issue of https://stackoverflow.com/questions/31698241/linking-error-when-compiling-crypto-for-armhf

To workaround that:

```
sudo ln -s /usr/ /usr/arm-linux-gnueabihf/usr
```
