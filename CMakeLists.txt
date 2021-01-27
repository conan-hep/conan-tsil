cmake_minimum_required(VERSION 3.1)
project(TSIL C)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

if(NOT TSIL_SIZE)
  set(TSIL_SIZE "TSIL_SIZE_LONG") # default
endif()

if(TSIL_SIZE STREQUAL "TSIL_SIZE_DOUBLE")
  add_definitions(-DTSIL_SIZE_DOUBLE)
elseif(TSIL_SIZE STREQUAL "TSIL_SIZE_LONG")
  add_definitions(-DTSIL_SIZE_LONG)
else()
  message(FATAL_ERROR "You must set TSIL_SIZE to either TSIL_SIZE_DOUBLE or TSIL_SIZE_LONG")
endif()

message(STATUS "Using ${TSIL_SIZE}")

add_library(tsil STATIC
  initialize.c
  evaluate.c
  fevaluate.c
  generic.c
  rk6.c
  rk5.c
  functions.c
  dilog.c
  trilog.c
  dBds.c
  dSds.c
  dTds.c
  dUds.c
  dsMds.c
  initB.c
  initS.c
  initT.c
  initU.c
  initV.c
  initM.c
  special.c
  analyticAB.c
  analyticI.c
  analyticS.c
  analyticT.c
  analyticTbar.c
  analyticU.c
  analyticV.c
  analyticM.c
  setTbar.c
  setV.c
  setbold.c
  )

add_executable(tsil.x basecalc.c)
target_link_libraries(tsil.x tsil m)
set_target_properties(tsil.x PROPERTIES OUTPUT_NAME "tsil")

add_executable(tsil.tst testprog.c)
target_link_libraries(tsil.tst tsil m)
