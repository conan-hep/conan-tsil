import os

from conans import ConanFile, CMake, Meson, tools


class TsilTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = ["cmake", "make", "pkg_config"]
    _meson_dir = "meson-build"
    _make_dir = "make-build"

    def _build_cmake(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options["TSIL"].fPIC
        cmake.configure()
        cmake.build()

    def _build_make(self):
        cmd = "make -f ..{}..{}Makefile".format(os.sep, os.sep)

        self.run("echo 'current directory: ' `pwd`")
        print(cmd)
        self.run(cmd)

    def _build_meson(self):
        meson = Meson(self)
        meson.configure(build_folder=self._meson_dir)
        meson.build()

    def build(self):
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        self._build_cmake()
        self._build_make()
        self._build_meson()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            with tools.chdir("bin"):
                self.run(".%stest_cmake" % os.sep)
            with tools.chdir(self._make_dir):
                self.run(".%stest_make" % os.sep)
            with tools.chdir(self._meson_dir):
                self.run(".%stest_meson" % os.sep)
