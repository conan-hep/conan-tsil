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
        march = ''

        if self.settings.arch == 'x86':
            march = '-m32'
        elif self.settings.arch == 'x86_64':
            march = '-m64'

        cxxflags = march

        cmd = "make CXXFLAGS='{}' -f {}{}Makefile".format(
            cxxflags,
            self.source_folder,
            os.sep)
        print(cmd)
        self.run(cmd)

    def _build_meson(self):
        meson = Meson(self)
        meson.configure(build_folder=self._meson_dir)
        meson.build()

    def build(self):
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
