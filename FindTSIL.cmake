# Distributed under the GPLv3 License.
# Author: Alexander Voigt
#
# FindTSIL
# -------------
#
# Finds the TSIL library.
# [https://www.niu.edu/spmartin/TSIL/]
#
# This module reads the following variables:
#
# CONAN_INCLUDE_DIRS_TSIL - directory of tsil.h
# CONAN_LIB_DIRS_TSIL     - directory of libtsil.a
#
# This module defines the following variables:
#
# TSIL_FOUND         - set if TSIL has been found
# TSIL_VERSION       - TSIL version
# TSIL_INCLUDE_DIRS  - TSIL include directory
# TSIL_LIBRARIES     - TSIL library
#
# and defines the following imported targets:
#
# TSIL::TSIL

message(STATUS "searching for tsil.h in ${CONAN_INCLUDE_DIRS_TSIL}")

# search tsil.h
find_path(TSIL_INCLUDE_DIRS
  NAMES tsil.h
  PATHS ${CONAN_INCLUDE_DIRS_TSIL}
)

message(STATUS "searching for tsil lib in ${CONAN_LIB_DIRS_TSIL}")

# search TSIL library
find_library(TSIL_LIBRARIES
  NAMES tsil
  PATHS ${CONAN_LIB_DIRS_TSIL}
)

# find version
if(TSIL_INCLUDE_DIRS)
  file(READ "${TSIL_INCLUDE_DIRS}/tsil.h" _tsil_header)

  string(REGEX MATCH "define[ \t]+TSIL_VERSION[ \t]+\"([0-9]+)\\.[0-9]+\"" _tsil_version_major_match "${_tsil_header}")
  set(TSIL_VERSION_MAJOR "${CMAKE_MATCH_1}")
  string(REGEX MATCH "define[ \t]+TSIL_VERSION[ \t]+\"[0-9]+\\.([0-9]+)\"" _tsil_version_minor_match "${_tsil_header}")
  set(TSIL_VERSION_MINOR "${CMAKE_MATCH_1}")

  set(TSIL_VERSION ${TSIL_VERSION_MAJOR}.${TSIL_VERSION_MINOR})

  if(TSIL_FIND_VERSION)
    if(TSIL_FIND_VERSION_EXACT AND NOT ${TSIL_VERSION} VERSION_EQUAL ${TSIL_FIND_VERSION})
      message(FATAL_ERROR "TSIL version ${TSIL_VERSION} found in ${TSIL_INCLUDE_DIRS}, "
        "but exact version ${TSIL_FIND_VERSION} is required.")
    elseif(${TSIL_VERSION} VERSION_LESS ${TSIL_FIND_VERSION})
      message(FATAL_ERROR "TSIL version ${TSIL_VERSION} found in ${TSIL_INCLUDE_DIRS}, "
        "but at least version ${TSIL_FIND_VERSION} is required.")
    endif()
  endif()
endif()

include(FindPackageHandleStandardArgs)

find_package_handle_standard_args(TSIL
  FOUND_VAR TSIL_FOUND
  REQUIRED_VARS
    TSIL_LIBRARIES
    TSIL_INCLUDE_DIRS
)

if(TSIL_FOUND AND NOT TARGET TSIL::TSIL)
  add_library(TSIL::TSIL UNKNOWN IMPORTED)
  set_target_properties(TSIL::TSIL PROPERTIES
    IMPORTED_LOCATION "${TSIL_LIBRARIES}"
    INTERFACE_INCLUDE_DIRECTORIES "${TSIL_INCLUDE_DIRS}"
  )
endif()

mark_as_advanced(
  TSIL_INCLUDE_DIRS
  TSIL_LIBRARIES
)
