from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps, cmake_layout
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

    requires = (
        "qt/5.15.8"
    )

    tool_requires = ("cmake/3.25.1",
                "ninja/1.11.0",
                "ccache/4.6",
                "swig/4.0.2",
                "cppcheck/2.9.3"
                )

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = {
                       "shared": False,
                       "fPIC": False,
                       #"qt:shared": "True",
                       #"qt:opengl": "no",
                    #    "qt:openssl": False,
                    #    "qt:with_pcre2": True,
                    #    "qt:with_freetype": True,
                    #    "qt:with_fontconfig": True,
                    #    "qt:with_icu": True,
                    #    "qt:with_libjpeg": "False",
                    #    "qt:with_libpng": False,
                    #    "qt:with_sqlite3": False,
                    #    "qt:with_mysql": False,
                    #    "qt:with_pq": False,
                    #    "qt:with_odbc": False,
                    #    "qt:with_openal": False,
                    #    "qt:with_zstd": True,
                    #    "qt:with_md4c": False,
                    #    "qt:gui": True,
                    #    "qt:widgets": True,
                    #    "qt:qtwayland": True
                    "qt:shared": True,
                    "qt:with_glib": False,
                    "qt:with_sqlite3": False,
                    "qt:with_mysql": False,
                    "qt:with_pq": False,
                    "qt:with_odbc": False,
                    "qt:qtsvg": True,
                    "qt:qtwayland": True,
                    "qt:opengl": "no",
    }

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        cmake = CMakeDeps(self)
        cmake.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.runenv_info.define("QT_QPA_PLATFORM", "wayland")