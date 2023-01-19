from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class Qt5ExampleConsumerConan(ConanFile):
    name = "qt5ExampleConsumer"
    version = "0.0.1"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Qt5ExampleConsumer here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }

    default_options = {
        "shared": False,
        "fPIC": True,
        # "qt:shared": True,
        # "qt:with_glib": False,
        # "qt:with_sqlite3": False,
        # "qt:with_mysql": False,
        # "qt:with_pq": False,
        # "qt:with_odbc": False,
        # "qt:qtsvg": True,
        "qt:qtwayland": True,
    }

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def requirements(self):
        self.requires("qt5Example/0.0.1")

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
