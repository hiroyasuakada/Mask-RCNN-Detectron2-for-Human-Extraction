# nvidia-docker run --rm -it -v /home/printeps2017a/akada_files:/home dockerfile:latest /bin/bash
xhost +local:user
    docker run -it \
    --runtime=nvidia \
    --env=DISPLAY=$DISPLAY \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --env="QT_X11_NO_MITSHM=1" \
    --rm \
    -p 8888:8888 \
    -v /home/ytpc2019b/catkin_ws/src/ros_start/scripts:/home \
    --net host \
    dockerfile:latest \