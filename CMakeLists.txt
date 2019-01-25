cmake_minimum_required(VERSION 2.8.3)
project(loam_velodyne_kitti_ros)

if(NOT DEFINED CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  nav_msgs
  sensor_msgs
  roscpp
  rospy
  std_msgs
  tf)

find_package(PCL 1.8 REQUIRED)
find_package(OpenCV REQUIRED)

include_directories(
  include
	${catkin_INCLUDE_DIRS} 
#	${EIGEN3_INCLUDE_DIR}
	${PCL_INCLUDE_DIRS})

catkin_package(
  CATKIN_DEPENDS geometry_msgs nav_msgs roscpp rospy std_msgs
  DEPENDS EIGEN3 PCL OpenCV
  INCLUDE_DIRS include
)


add_executable(scanRegistrationKittiRos src/scanRegistrationKittiRos.cpp)
target_link_libraries(scanRegistrationKittiRos ${catkin_LIBRARIES} ${PCL_LIBRARIES} ${OpenCV_LIBS})

add_executable(laserOdometryKittiRos src/laserOdometryKittiRos.cpp)
target_link_libraries(laserOdometryKittiRos ${catkin_LIBRARIES} ${PCL_LIBRARIES} ${OpenCV_LIBS})

add_executable(laserMappingKittiRos src/laserMappingKittiRos.cpp)
target_link_libraries(laserMappingKittiRos ${catkin_LIBRARIES} ${PCL_LIBRARIES} ${OpenCV_LIBS})

add_executable(transformMaintenanceKittiRos src/transformMaintenanceKittiRos.cpp)
target_link_libraries(transformMaintenanceKittiRos ${catkin_LIBRARIES} ${PCL_LIBRARIES} ${OpenCV_LIBS})
