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

##### Please note that if you want to extract other objects or only humans, please edit [this line](https://github.com/hiroyasuakada/Mask-RCNN-Detectron2-for-Object-Extraction/blob/44d9d90fd9ff50df769c11bfe06a6ce15afd5bef/detectron2_repo_with_revision/detectron2/utils/visualizer.py#L623) accordingly.

### 1. Use [Dockerfile](<https://github.com/hiroyasuakada/mask-processing/tree/master/docker_mask_processing/>) to install requirements

    ./build.sh

and then run docker container.

Current directory should be 'workplace' and my main directory is 'mask-processing'.

### 2. Download a pre-trained model from [Detectron2 Model ZOO](<https://github.com/facebookresearch/detectron2/blob/master/MODEL_ZOO.md/>) 

My system is using pkl file of *Mask R-CNN X152*, so download it. 
Then, put it into configs of mask-processing directory.

'cascade_mask_rcnn_X_152_32x8d_FPN_IN5k_gn_dconv.pkl'

    mv (pkl file) ./mask-processing/detectron2_repo_with_revision/configs/model/

Note that if you want to use other pre-trained weights (pkl file), please change the path in [my code here](https://github.com/hiroyasuakada/Mask-RCNN-Detectron2-for-Human-Extraction/blob/fa00e92835b0931e09b7c08947197ee04cf8694d/process.py#L33).

### 3. Prepare .jpg images in 'input_image' directory (possible to process multiple images)

### 4. Run process.py

    python3 process.py
    
or
    
    python process.py
    

### 5. Get 4 types of images in 'output_image' directory


## References
[Detectron2 Facebook AI Research's next generation software system](https://github.com/facebookresearch/detectron2)
