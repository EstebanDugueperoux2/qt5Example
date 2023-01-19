from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
from conan.tools.files import rm
from conans import tools

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
        "shared": False,
        "fPIC": True,
        # "qt:opengl": "no",
        # "qt:openssl": False,
        # "qt:with_freetype": False,
        # "qt:with_libjpeg": False,
        # "qt:with_libpng": False,
        # "qt:with_sqlite3": False,
        # "qt:with_mysql": False,
        # "qt:with_pq": False,
        # "qt:with_odbc": False,
        # "qt:with_zstd": False,
        # "qt:gui": False,
        # "qt:widgets": False,
        "qt:qtwayland": True,
    }

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"
    
    def requirements(self):
        self.requires("boost/1.81.0")
        self.requires("glog/0.6.0")
        self.requires("grpc/1.50.1")
        self.requires("protobuf/3.21.4")
        self.requires("zlib/1.2.13", override=True)
        self.requires('qt/5.15.8')

    def build_requirements(self):
        self.tool_requires("cmake/3.25.0")
        self.tool_requires("ninja/1.11.1")
        self.tool_requires("ccache/4.6")
        self.tool_requires("protobuf/3.21.4")
        self.tool_requires("grpc/1.50.1")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self, generator="Ninja")
        tc.generate()

        deps = CMakeDeps(self)
        # Usefull in case of cross compilation, see https://docs.conan.io/en/latest/reference/conanfile/tools/cmake/cmakedeps.html#build-context-activated
        deps.build_context_activated = ["cmake", "ninja", "ccache", "protobuf", "grpc"]
        deps.build_context_build_modules = ["protobuf", "grpc"]
        # Usefull in case of cross compilation, see https://docs.conan.io/en/latest/reference/conanfile/tools/cmake/cmakedeps.html#build-context-suffix
        # To avoid ".conan/data/protobuf/3.21.4/_/_/package/6eac640ec9164ae7f9e2edf0bcb00e092769a96d/bin/protoc: Exec format error`" errot
        deps.build_context_suffix = {"protobuf": "_BUILD", "grpc": "_BUILD"}
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    # def package_info(self):
    #     self.cpp_info.requires = ['wayland::wayland']