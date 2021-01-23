# Mask-RCNN-Detectron2-for-Human-Extraction

## Description

Application to extract humans and their belongings (bags, etc.) in images based on a pre-trained model of [Mask R-CNN (Detectron2)](https://github.com/facebookresearch/detectron2). 

Please see examples of extracting "humans and handbags" below.

If you want to extract other objects or only humans, please edit [this line](https://github.com/hiroyasuakada/Mask-RCNN-Detectron2-for-Object-Extraction/blob/44d9d90fd9ff50df769c11bfe06a6ce15afd5bef/detectron2_repo_with_revision/detectron2/utils/visualizer.py#L623) accordingly.

## Demo

### 1. Preparing images (possible to process multiple images)

<div align="center">
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/input_image/test_input.jpg" alt="属性" title="タイトル">
</div>

<br>

### 2. Producing four types of the images after the mask process
 
<div align="center">
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/image_with_full_prediction/test_output.jpg" alt="属性">
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/image_with_mask_cropped/test_output.jpg" alt="属性">
<div align="center">
image_with_full_prediction　　 　　image_with_mask_cropped
</div>

<br>

<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/cropped_figure/test_output.jpg" alt="属性">
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/binary_mask/test_output.jpg" alt="属性">
<div align="center">
binary_mask　　　　　　 　　 　cropped_figure
</div>

</div>

<br>

## Usage

### 1. Clone this repository

    git clone https://github.com/hiroyasuakada/Mask-RCNN-Detectron2-for-Human-Extraction.git

### 2. Use [Dockerfile](<https://github.com/hiroyasuakada/mask-processing/tree/master/docker_mask_processing/>) in the 'docker_mask_processing' direcotry to install requirements for Detectron2.

    ./build.sh

and then run docker container.

Current directory should be 'temporary_workspace'.

### 2. Download a pre-trained model from [Detectron2 Model ZOO](<https://github.com/facebookresearch/detectron2/blob/master/MODEL_ZOO.md/>) 

Please download the pre-trained weights, and then put it into configs of the 'detectron2_repo_with_revision' directory.

    mv (pkl file) ./Mask-RCNN-Detectron2-for-Human-Extraction/detectron2_repo_with_revision/configs/model/

Currently, my system is using "cascade_mask_rcnn_X_152_32x8d_FPN_IN5k_gn_dconv.pkl". 

If you want to use other pre-trained weights, please change the path in [my code here](https://github.com/hiroyasuakada/Mask-RCNN-Detectron2-for-Human-Extraction/blob/fa00e92835b0931e09b7c08947197ee04cf8694d/process.py#L33). 

### 3. Prepare .jpg images in 'input_image' directory (possible to process multiple images)

    mkdir input_image

### 4. Run process.py

    python3 process.py
    
#### Please note that if you want to extract other objects or only humans, please edit [this line](https://github.com/hiroyasuakada/Mask-RCNN-Detectron2-for-Object-Extraction/blob/44d9d90fd9ff50df769c11bfe06a6ce15afd5bef/detectron2_repo_with_revision/detectron2/utils/visualizer.py#L623) accordingly.

### 5. Get 4 types of images in 'output_image' directory


## References
[Detectron2 Facebook AI Research's next generation software system](https://github.com/facebookresearch/detectron2)
