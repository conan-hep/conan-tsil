[![Build Status Travis](https://travis-ci.org/conan-hep/conan-tsil.svg)](https://travis-ci.org/conan-hep/conan-tsil)

## Conan package recipe for [*TSIL*](https://www.niu.edu/spmartin/TSIL/)

Stephen P. Martin, David G. Robertson, *TSIL: A Program for the
calculation of two-loop self-energy integrals*,
[*Comput.Phys.Commun.* **174** (2006) 133-151](https://inspirehep.net/record/675010)
[arXiv:hep-ph/0501132](https://arxiv.org/abs/hep-ph/0501132)

## For users

### Installation of dependencies

TSIL can be installed with conan by running:

    conan install TSIL/1.44@conan/stable

Alternatively a `conanfile.txt` file can be created in your project
directory with the following content:

    [requires]
    TSIL/1.44@conan/stable

    [generators]
    cmake
    make
    pkg_config

The dependencies of your project are then installed by running:

    mkdir build
    cd build
    conan install ..

### Building your project

Afterwards the project can be configured via CMake and build with
`make` by running:

    cmake ..
    make

Alternatively the project can be configured with Meson and build with
`ninja` by running:

    export PKG_CONFIG_PATH=.
    meson ..
    ninja

Alternatively the project can be build with `make` by running:

    make -f ../Makefile

A complete example can be found in the `examples/` directory.


## Build and package

The following command both runs all the steps of the conan file, and
publishes the package to the local system cache.  This includes
downloading dependencies from `build_requires` and `requires`, and
then running the `build()` method.

    $ conan create . conan/stable


### Available Options

| Option        | Default          | Possible Values                          |
| ------------- |------------------|------------------------------------------|
| fPIC          | True             |  [True, False]                           |
| TSIL_SIZE     | TSIL_SIZE_LONG   |  [TSIL_SIZE_LONG, TSIL_SIZE_DOUBLE]      |


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this
recipe, which can be used to build and package TSIL.  It does *not* in
any way apply or is related to the actual software being packaged.

[MIT](LICENSE)
