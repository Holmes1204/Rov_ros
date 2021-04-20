# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "topic_example: 1 messages, 0 services")

set(MSG_I_FLAGS "-Itopic_example:/home/holmes/ros_ws/EngCom/src/ros_serial/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(topic_example_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/holmes/ros_ws/EngCom/src/ros_serial/msg/Img_fb.msg" NAME_WE)
add_custom_target(_topic_example_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "topic_example" "/home/holmes/ros_ws/EngCom/src/ros_serial/msg/Img_fb.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(topic_example
  "/home/holmes/ros_ws/EngCom/src/ros_serial/msg/Img_fb.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/topic_example
)

### Generating Services

### Generating Module File
_generate_module_cpp(topic_example
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/topic_example
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(topic_example_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(topic_example_generate_messages topic_example_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/holmes/ros_ws/EngCom/src/ros_serial/msg/Img_fb.msg" NAME_WE)
add_dependencies(topic_example_generate_messages_cpp _topic_example_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(topic_example_gencpp)
add_dependencies(topic_example_gencpp topic_example_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS topic_example_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(topic_example
  "/home/holmes/ros_ws/EngCom/src/ros_serial/msg/Img_fb.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/topic_example
)

### Generating Services

### Generating Module File
_generate_module_eus(topic_example
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/topic_example
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(topic_example_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(topic_example_generate_messages topic_example_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/holmes/ros_ws/EngCom/src/ros_serial/msg/Img_fb.msg" NAME_WE)
add_dependencies(topic_example_generate_messages_eus _topic_example_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(topic_example_geneus)
add_dependencies(topic_example_geneus topic_example_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS topic_example_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(topic_example
  "/home/holmes/ros_ws/EngCom/src/ros_serial/msg/Img_fb.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/topic_example
)

### Generating Services

### Generating Module File
_generate_module_lisp(topic_example
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/topic_example
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(topic_example_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(topic_example_generate_messages topic_example_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/holmes/ros_ws/EngCom/src/ros_serial/msg/Img_fb.msg" NAME_WE)
add_dependencies(topic_example_generate_messages_lisp _topic_example_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(topic_example_genlisp)
add_dependencies(topic_example_genlisp topic_example_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS topic_example_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(topic_example
  "/home/holmes/ros_ws/EngCom/src/ros_serial/msg/Img_fb.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/topic_example
)

### Generating Services

### Generating Module File
_generate_module_nodejs(topic_example
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/topic_example
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(topic_example_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(topic_example_generate_messages topic_example_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/holmes/ros_ws/EngCom/src/ros_serial/msg/Img_fb.msg" NAME_WE)
add_dependencies(topic_example_generate_messages_nodejs _topic_example_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(topic_example_gennodejs)
add_dependencies(topic_example_gennodejs topic_example_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS topic_example_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(topic_example
  "/home/holmes/ros_ws/EngCom/src/ros_serial/msg/Img_fb.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/topic_example
)

### Generating Services

### Generating Module File
_generate_module_py(topic_example
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/topic_example
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(topic_example_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(topic_example_generate_messages topic_example_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/holmes/ros_ws/EngCom/src/ros_serial/msg/Img_fb.msg" NAME_WE)
add_dependencies(topic_example_generate_messages_py _topic_example_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(topic_example_genpy)
add_dependencies(topic_example_genpy topic_example_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS topic_example_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/topic_example)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/topic_example
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(topic_example_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/topic_example)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/topic_example
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(topic_example_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/topic_example)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/topic_example
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(topic_example_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/topic_example)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/topic_example
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(topic_example_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/topic_example)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/topic_example\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/topic_example
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(topic_example_generate_messages_py std_msgs_generate_messages_py)
endif()
