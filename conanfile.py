from conan import ConanFile
from conan.tools.env import VirtualRunEnv
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
from conan.tools.files import copy

class qt5exampleConan(ConanFile):
    name = "qt5example"
    version = "0.0.1"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Qt5Example here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    package_type = "application"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }

    default_options = {
        "shared": False,
        "fPIC": True,
    }

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"
    
    def configure(self):
        self.options["*"].shared = self.options.shared
    
    def requirements(self):
        #self.requires('boost/1.81.0')
        self.requires('qt/5.15.14')
        # self.requires('qt/6.5.0')
        # self.requires("zlib/1.2.12", override=True)
        # self.requires("libffi/3.4.4", override=True)

    def build_requirements(self):
        self.tool_requires("cmake/3.30.1")
        self.tool_requires("ninja/1.12.1")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self, generator="Ninja")
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()
        
        ms = VirtualRunEnv(self)
        ms.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def deploy(self):
        self.output.info("deploy")
        copy(self, "*", src=self.package_folder, dst=self.deploy_folder)
