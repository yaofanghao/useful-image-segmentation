#!/bin/bash

rosrun dynamic_reconfigure dynparam set /camera/driver data_skip 3

rosbag record -O subset /amcl/parameter_descriptions \
/patrol_start \
/amcl/parameter_updates \
/amcl_pose \
/base_pose_ground_truth \
/clicked_point \
/clock \
/initialpose \
/map \
/map_metadata \
/map_updates \
/mobile_base/mobile_base_controller/cmd_vel \
/mobile_base/mobile_base_controller/odom \
/move_base/cancel \
/move_base/feedback \
/move_base/goal \
/move_base/result \
/move_base/status \
/move_base_node/DWAPlannerROS/cost_cloud \
/move_base_node/DWAPlannerROS/global_plan \
/move_base_node/DWAPlannerROS/local_plan \
/move_base_node/DWAPlannerROS/parameter_descriptions \
/move_base_node/DWAPlannerROS/parameter_updates \
/move_base_node/DWAPlannerROS/trajectory_cloud \
/move_base_node/NavfnROS/plan \
/move_base_node/current_goal \
/move_base_node/global_costmap/costmap \
/move_base_node/global_costmap/costmap_updates \
/move_base_node/global_costmap/footprint \
/move_base_node/global_costmap/inflation_layer/parameter_descriptions \
/move_base_node/global_costmap/inflation_layer/parameter_updates \
/move_base_node/global_costmap/obstacle_layer/parameter_descriptions \
/move_base_node/global_costmap/obstacle_layer/parameter_updates \
/move_base_node/global_costmap/parameter_descriptions \
/move_base_node/global_costmap/parameter_updates \
/move_base_node/global_costmap/static_layer/parameter_descriptions \
/move_base_node/global_costmap/static_layer/parameter_updates \
/move_base_node/local_costmap/costmap \
/move_base_node/local_costmap/costmap_updates \
/move_base_node/local_costmap/footprint \
/move_base_node/local_costmap/inflation_layer/parameter_descriptions \
/move_base_node/local_costmap/inflation_layer/parameter_updates \
/move_base_node/local_costmap/obstacle_layer/parameter_descriptions \
/move_base_node/local_costmap/obstacle_layer/parameter_updates \
/move_base_node/local_costmap/parameter_descriptions \
/move_base_node/local_costmap/parameter_updates \
/move_base_node/parameter_descriptions \
/move_base_node/parameter_updates \
/move_base_simple/goal \
/particlecloud \
/patrol_load/cancel \
/patrol_load/feedback \
/patrol_load/goal \
/patrol_load/result \
/patrol_load/status \
/patrol_nav/cancel \
/patrol_nav/feedback \
/patrol_nav/goal \
/patrol_nav/result \
/patrol_nav/status \
/patrol_points \
/patrol_state \
/patrol_points_array \
/rgbd_scan_filtered \
/rosout \
/rosout_agg \
/scan \
/tf \
/tf_static \
/camera/depth/camera_info \
/camera/rgb/camera_info \
/camera/rgb/image_raw \
/camera/depth/image_raw \


