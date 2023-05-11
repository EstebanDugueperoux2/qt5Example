# Conan Qt5 example

```
conan new -d name=qt5Example -d version=0.0.1 -f cmake_lib
```

## Steps to create a conan package with gcc10 profile

```
docker run --memory=10g --cpus=10 --rm -ti -v $PWD/deployement/:/home/conan/deployment/ conanio/gcc13-ubuntu18.04
<!-- docker exec -it alicevision_conan_client_1 bash -->
sudo apt -y update
sudo apt install -y python3-pip cmake ninja-build git vim pkg-config
sudo pip install --upgrade "conan"
git clone https://github.com/EstebanDugueperoux2/qt5Example.git
cd qt5Example

conan create . -o "*/*:shared=True" --profile:build .conan/profiles/gcc10 --profile:host .conan/profiles/gcc10 --build missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True

conan install . -o "*/*:shared=True" --profile:build .conan/profiles/gcc10 --profile:host .conan/profiles/gcc10 --deployer=runtime_deploy  --deployer-package=* --deployer-folder=../deployment

cd ..deployment/


```

## Steps to create a conan package with arm cross compilation 

```
docker run --rm -ti -v ${PWD}/.conan/:/home/conan/.conan/:z -v ${PWD}:/home/conan/project:z conanio/gcc10-ubuntu18.04
sudo apt -y update && sudo apt install -y crossbuild-essential-armhf qemu
cd project
sudo pip install --upgrade "conan<2"
conan create . --profile:build .conan/profiles/gcc12 --profile:host .conan/profiles/linux-armv7hf-gcc7 --build missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True
```

## Steps to create a conan package with mingw cross compilation 

```
docker run --rm -ti -v ${PWD}/.conan/:/home/conan/.conan/:z -v ${PWD}:/home/conan/project:z conanio/gcc12-ubuntu18.04
sudo apt -y update && sudo apt install -y g++-mingw-w64 wine
cd project
sudo pip install --upgrade "conan<2"
conan create . --profile:build .conan/profiles/gcc12 --profile:host .conan/profiles/mingw64 --build missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True
```
