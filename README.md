# mask-processing

## Description

End-to-End application to extract humans in images based on pre-trained model of [Mask R-CNN (Detectron2)](https://github.com/facebookresearch/detectron2). Please see examples below.

## Demo

### 1. Preparing images (possible to process multiple images)

<div align="center">
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/input_image/test.jpg" alt="属性" title="タイトル">
</div>

<br>

### 2. Producing four types of the images with mask

<div align="center">
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/image_with_full_prediction/test.jpg" alt="属性">
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/image_with_mask_cropped/test.jpg" alt="属性">
<div align="center">
image_with_full_prediction　　　　　　　image_with_mask_cropped
</div>

<br>
<br>

<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/binary_mask/test.jpg" alt="属性">
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/cropped_figure/test.jpg" alt="属性">
<div align="center">
binary_mask　　　　　　　　　　　　　　　cropped_figure
</div>

</div>

<br>

## Usage

### 1. Using [Dockerfile](<https://github.com/hiroyasuakada/mask-processing/tree/master/docker_mask_processing/>) to install requirements

    ./build.sh
    ./run.sh

Current directory should be 'workplace' and my main directory is 'mask-processing'.

### 2. Download a pre-trained model from [Detectron2 Model ZOO](<https://github.com/facebookresearch/detectron2/blob/master/MODEL_ZOO.md/>) 

My system is using pkl file of *Mask R-CNN X152*, so please download it. 
Then, put it into configs of mask-processing directory.

    mv (pkl file) ./mask-processing/detectron2_repo_with_revision/configs/model/

### 3. Preparing .jpg images in 'input_image' directory (possible to process multiple images)

### 4. Run process.py

    python3 process.py
    
or
    
    python process.py

### 5. Getting 4 types of images in 'output_image' directory


## References
[Detectron2 Facebook AI Research's next generation software system](https://github.com/facebookresearch/detectron2)
