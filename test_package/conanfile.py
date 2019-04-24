import os

from conans import ConanFile, CMake, tools


class TsilTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = ["cmake", "make"]

    def _build_cmake(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options["TSIL"].fPIC
        cmake.configure()
        cmake.build()

    def _build_make(self):
        self.run("make -f ..{}..{}Makefile".format(os.sep, os.sep))

    def build(self):
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        self._build_cmake()
        self._build_make()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run(".%stest_cmake" % os.sep)
            self.run(".%stest_make" % os.sep)
