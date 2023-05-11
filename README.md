# Conan Qt5 example

```
conan new qt5Example/0.0.1 --template=cmake_exe
```

## Steps to create a conan package with gcc8 profile

```
docker run --rm -ti -v ${PWD}/.conan/:/home/conan/.conan/:z -v ${PWD}:/home/conan/project:z conanio/gcc10-ubuntu18.04
cd project
sudo pip install --upgrade "conan<2"

 sudo apt -y update && \
    sudo apt install -y \
            xkb-data \
            libice-dev \
            libsm-dev \
            libfontenc-dev \
            libxaw7-dev \
            libxcomposite-dev \
            libxcursor-dev \
            libxdmcp-dev \
            libxi-dev \
            libxinerama-dev \
            libxkbfile-dev \
            libxrandr-dev \
            libxres-dev \
            libxcb-screensaver0-dev \
            xscreensaver \
            libxtst-dev \
            libxv-dev \
            libxvmc-dev \
            xtrans-dev \
            libxcb1-dev \
            libxmuu-dev \
            libxss-dev \
            libxdg-basedir-dev \
            libxft-dev \
            libxcb-xkb-dev \
            libxcb-icccm4-dev \
            libxcb-image0-dev \
            libxcb-keysyms1-dev \
            libkwinxrenderutils11 \
            libxcb-cursor-dev \
            libxcb-render-util0-dev \
            libxcb-xinerama0-dev \
            libxcb-util0-dev \
            libcups2-dev \
            python2.7 \
            libgl-dev \
            uuid-dev 


conan create . --profile:build .conan/profiles/gcc10 --profile:host .conan/profiles/gcc10 --build missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True
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
