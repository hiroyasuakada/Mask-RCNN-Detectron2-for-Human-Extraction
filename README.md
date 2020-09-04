# mask-processing

# Description


# Demo

1. Preparing images

<div align="center">
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/input_image/test.jpg" alt="属性" title="タイトル">
</div>

<br>

2. Processing images with mask

<div align="center">
  <img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/image_with_full_prediction/test.jpg" alt="属性">
  <figcaption>{{ 属性 }}</figcaption>
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/image_with_mask_cropped/test.jpg" alt="属性">
  <br>
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/binary_mask/test.jpg" alt="属性">
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/cropped_figure/test.jpg" alt="属性">
</div>

<br>

# Usage

## 1. Install [Detectron2](<https://github.com/facebookresearch/detectron2/>)

please see INSTALL.md. in the Installation section.
Using its dockerfile is highly recommended.

## 2. Download a pre-trained model from [Detectron2 Model ZOO](<https://github.com/facebookresearch/detectron2/blob/master/MODEL_ZOO.md/>) 

My system is using *Mask R-CNN X152*, so please download it.


## 3. Clone this repository

    git clone https://github.com/hiroyasuakada/mask-processing.git

## 4. Preparing .jpg images in 'input_image' directory

## 5. Run process.py

    python3 process.py
    
or
    
    python process.py

## 6. Getting 4 types of images in 'output_image' directory



# References
[Detectron2 Facebook AI Research's next generation software system](https://github.com/facebookresearch/detectron2)
