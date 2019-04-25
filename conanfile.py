from conans import ConanFile, tools
from conans.errors import ConanException

class TsilConan(ConanFile):
    name = "TSIL"
    version = "1.44"
    license = "GPL-2.0-or-later"
    author = "Alexander Voigt"
    url = "https://www.niu.edu/spmartin/TSIL/"
    description = "Two-loop Self-energy Integral Library"
    topics = ("HEP")
    settings = "os", "compiler", "build_type", "arch"
    options = {"fPIC": [True, False],
               "TSIL_SIZE": ["TSIL_SIZE_LONG", "TSIL_SIZE_DOUBLE"]}
    exports = ["LICENSE", "FindTSIL.cmake"]
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

    def build(self):
        with tools.chdir(self._source_subfolder):
            march = '-march=native'

            if self.settings.arch == 'x86':
                march = '-m32'
            elif self.settings.arch == 'x86_64':
                march = '-m64'

            cmd = "make CC='{}' TSIL_SIZE='-D{}' TSIL_OPT='-O3 {} {}'".format(
                self.settings.compiler,
                self.options.TSIL_SIZE,
                march,
                "-fPIC" if self.options.fPIC else "")

            print(cmd)
            self.run(cmd)

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy('FindTSIL.cmake', '.', '.')

    def package_info(self):
        self.cpp_info.libs = ["tsil"]
        self.cpp_info.defines.append(str(self.options.TSIL_SIZE))
