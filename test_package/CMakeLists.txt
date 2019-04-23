cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(test_tsil test_tsil.cpp)
target_link_libraries(test_tsil ${CONAN_LIBS})
target_include_directories(test_tsil ${CONAN_INCLUDE_DIRS})

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME test_tsil
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND test_tsil)
