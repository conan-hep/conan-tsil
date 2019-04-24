## Conan package recipe for [*TSIL*](https://www.niu.edu/spmartin/TSIL/)


## For Users

### Basic setup

    $ conan install tsil/1.44@conan/stable

### Project setup

In your `conanfile.txt` file (located in your project directly) add
the following lines:

    [requires]
    TSIL/1.44@conan/stable

    [generators]
    cmake
    make
    pkg_config

Install the dependencies for your project by running:

    mkdir build
    cd build
    conan install ..

Afterwards the project can be configured via CMake by running:

    cmake ..
    make

A complete example can be found in the `test_package_extern/`
directory.


## Build and package

The following command both runs all the steps of the conan file, and
publishes the package to the local system cache.  This includes
downloading dependencies from "build_requires" and "requires" , and
then running the build() method.

    $ conan create . conan/stable


### Available Options

| Option        | Default          | Possible Values                          |
| ------------- |------------------|------------------------------------------|
| fPIC          | True             |  [True, False]                           |
| TSIL_SIZE     | "TSIL_SIZE_LONG" |  ["TSIL_SIZE_LONG", "TSIL_SIZE_DOUBLE"]  |


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this
recipe, which can be used to build and package TSIL.  It does *not* in
any way apply or is related to the actual software being packaged.

[MIT](LICENSE)
