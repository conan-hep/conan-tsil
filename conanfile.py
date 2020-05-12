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
    exports = ["LICENSE"]
    default_options = "fPIC=True", "TSIL_SIZE=TSIL_SIZE_LONG"
    generators = ["cmake", "make", "pkg_config"]
    _source_subfolder = "tsil-{}".format(version)

    def configure(self):
        if self.settings.os == "Windows":
            raise ConanException("Windows not supported")

    def source(self):
        mirrors = [
            "http://www.niu.edu/spmartin/TSIL/tsil-{}.tar.gz",
            "http://faculty.otterbein.edu/DRobertson/tsil/tsil-{}.tar.gz"
        ]

        try:
            tools.get(mirrors[0].format(self.version))
        except ConanException:
            tools.get(mirrors[1].format(self.version))

    def _get_cc(self):
        if tools.is_apple_os(self.settings.os):
            xcrun = tools.XCRun(self.settings)
            return xcrun.find("clang")
        return self.settings.compiler

    def _get_march(self):
        march = ''
        if self.settings.arch == 'x86':
            march = '-m32'
        elif self.settings.arch == 'x86_64':
            march = '-m64'
        return march

    def build(self):
        with tools.chdir(self._source_subfolder):
            cmd = "make -j{} CC='{}' TSIL_SIZE='-D{}' TSIL_OPT='-O3 {} {}'".format(
                tools.cpu_count(),
                self._get_cc(),
                self.options.TSIL_SIZE,
                self._get_march(),
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
        self.copy("LICENSE.txt", src=self._source_subfolder, dst="licenses", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["tsil"]
        self.cpp_info.defines.append(str(self.options.TSIL_SIZE))
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("m")
