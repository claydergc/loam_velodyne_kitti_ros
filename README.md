# loam_velodyne_kitti_ros
This package is a modified copy of the ROS Indigo versions of the LOAM algorithm to work with the KITTI dataset.:

[loam_velodyne](http://docs.ros.org/indigo/api/loam_velodyne/html/files.html)
[loam_back_and_forth](http://docs.ros.org/indigo/api/loam_back_and_forth/html/files.html)
[loam_velodyne](http://docs.ros.org/indigo/api/loam_continuous/html/files.html)
 
Main changes have been done in:
 
scanRegistration.cpp renamed to scanRegistrationKittiROS.cpp

where at the end of this file the KITTI Dataset is published by reading the .bin files and converting it to point cloud data.

Additionally, point clouds from each .bin file are published in a lower rate (4 Hz, which depends on the speed of your computer). This was done because in the experiments done with my computer the original rate of the LiDAR was making the LOAM algorithm drop some point clouds, which resulted in an incorrect trajectory.
 
Also, transformToEnd() and transformToStart() functions have been modified since the KITTI Dataset is distorsion free.

The separation of the Velodyne HDL-64's rings have been done according to [laboshinl's code](https://github.com/laboshinl/loam_velodyne)

Before building the project, it is important to consider the KITTI Dataset file structure. All the KITTI dataset need to be in a same folder. This folder should have the following structure:

```bash
.
├── data_odometry_calib                  
├── data_odometry_poses
└── data_odometry_velodyne
```

data_odometry_calib contains the files: calib.txt and times.txt for each sequence.  
data_odometry_poses contains the ground truth files for each sequence.  
data_odometry_velodyne contains the .bin files for each sequence.  

All previously mentioned folders have inside the same structure as downloaded from the KITTI website.


How to build:

```
$ cd catkin_ws
$ catkin_make
```

Running:
```
$ roslaunch loam_velodyne_kitti_ros loam_velodyne_kitti_ros.launch 
```
