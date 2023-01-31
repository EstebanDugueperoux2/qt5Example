from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
from conan.tools.files import rm

class Qt5ExampleConan(ConanFile):
    name = "qt5Example"
    version = "0.0.1"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Qt5Example here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }

    default_options = {
        "shared": True,
        "fPIC": True,
        # "qt:cross_compile": "/usr/bin/arm-linux-gnueabihf-",
        # "qt:device": "linux-arm-generic-g++",
        # "qt:config": "-device-option DISTRO_OPTS=hard-float -extprefix",
        # "qt:sysroot": "/usr/arm-linux-gnueabihf/",
        # "qt:qtx11extras": False,
        
        "qt:shared": True,
        "qt:opengl": "no",
        "qt:with_harfbuzz": False,
        "qt:with_libjpeg": False,
        "qt:with_libpng": False,
        "qt:with_sqlite3": False,
        "qt:with_mysql": False,
        "qt:with_pq": False,
        "qt:with_odbc": False,
        "qt:with_openal": False,
        "qt:with_md4c": True,
        "qt:with_x11": False,
        "qt:gui": False,
        "qt:widgets": False,
    }

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"
    
    def requirements(self):
        self.requires('qt/5.15.8')

    def build_requirements(self):
        self.tool_requires("cmake/3.25.0")
        self.tool_requires("ninja/1.11.1")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self, generator="Ninja")
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()