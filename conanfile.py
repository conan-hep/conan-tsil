import os
from conans import ConanFile, CMake, tools
import shutil

class TsilConan(ConanFile):
    name = "TSIL"
    version = "1.45"
    license = "GPL-2.0-or-later"
    author = "Alexander Voigt"
    url = "https://www.niu.edu/spmartin/TSIL/"
    description = "Two-loop Self-energy Integral Library"
    topics = ("HEP")
    settings = "os", "compiler", "build_type", "arch"
    options = {"fPIC": [True, False],
               "TSIL_SIZE": ["TSIL_SIZE_LONG", "TSIL_SIZE_DOUBLE"]}
    exports = ["LICENSE", "CMakeLists.txt"]
    default_options = "fPIC=True", "TSIL_SIZE=TSIL_SIZE_LONG"
    generators = ["cmake", "make", "pkg_config"]
    _source_subfolder = "tsil-{}".format(version)

    def source(self):
        mirrors = [
            "http://www.niu.edu/spmartin/TSIL/tsil-{}.tar.gz",
            "http://faculty.otterbein.edu/DRobertson/tsil/tsil-{}.tar.gz"
        ]

        try:
            tools.get(mirrors[0].format(self.version))
        except ConanException:
            tools.get(mirrors[1].format(self.version))

        shutil.copyfile("CMakeLists.txt", "{}{}CMakeLists.txt".format(self._source_subfolder, os.sep))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("LICENSE.txt", src=self._source_subfolder, dst="licenses", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["tsil"]
        self.cpp_info.defines.append(str(self.options.TSIL_SIZE))
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("m")
