cmake_minimum_required(VERSION 2.8.12)
project(PackageTest C CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(TSIL REQUIRED)

add_executable(test_cmake test_tsil.cpp)
target_link_libraries(test_cmake TSIL::TSIL)

add_executable(test_cmake_c test_tsil.c)
target_link_libraries(test_cmake_c TSIL::TSIL m)
