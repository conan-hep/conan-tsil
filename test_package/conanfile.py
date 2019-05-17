import os

from conans import ConanFile, CMake, tools


class TsilTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = ["cmake"]

    def _build_cmake(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options["TSIL"].fPIC
        cmake.configure()
        cmake.build()

    def build(self):
        self._build_cmake()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            with tools.chdir("bin"):
                self.run(".%stest_cmake" % os.sep)
                self.run(".%stest_cmake_c" % os.sep)
