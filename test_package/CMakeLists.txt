cmake_minimum_required(VERSION 2.8.12)
project(PackageTest C CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(test_cmake test_tsil.cpp)
target_link_libraries(test_cmake CONAN_PKG::TSIL)

add_executable(test_cmake_c test_tsil.c)
target_link_libraries(test_cmake_c CONAN_PKG::TSIL m)
