## Conan package recipe for [*TSIL*](https://www.niu.edu/spmartin/TSIL/)


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
