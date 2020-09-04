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
  <img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/image_with_full_prediction/test.jpg" alt="属性" title="fff">
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/image_with_mask_cropped/test.jpg" alt="属性" title="タイトル">
  <br>
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/binary_mask/test.jpg" alt="属性" title="タイトル">
<img src="https://github.com/hiroyasuakada/mask-processing/blob/master/demo/output_image/cropped_figure/test.jpg" alt="属性" title="タイトル">
</div>

<br>

# Application Architecture

<div align="center">
<img src="https://github.com/hiroyasuakada/dynamic-object-removal-with-unpaired-images/blob/master/demo/GraphicalAbstract1.png" alt="属性" title="タイトル">
</div>

<div align="center">
Block diagram of our application
</div>

<br>

**Training:** In the cycle process, for the given images with a human in
domain X and images without a human in domain Y , the generator G tries to create non-occluded images of G(x) that are
indistinguishable from the images in Y and the discriminator Dy tries to distinguish the fake from the real images, where
adversarial loss is calculated. Then, the generator F tries to generate indistinguishable images of F(y) from the images
in X, where cycle consistency loss is calculated (and vice versa). In the mask process, mask images are extracted from
the ones in X and used to cut out the human-shaped area of both images in X and G(x), yielding images of Xmask and
G(x)mask. Then, we compute MSE loss between the images of Xmask and the corresponding G(x)mask images. 

**Testing:** The generator G is used to translate occluded images into realistic static images without the farmer to evaluate the quality
of the generated images.

<br>

# Dataset

<div align="center">
<img src="https://github.com/hiroyasuakada/dynamic-object-removal-with-unpaired-images/blob/master/demo/domain_X_Y_small.png" alt="属性" title="タイトル">
</div>

<div align="center">
Examples of our dataset: images with a farmer in domain X (left) and images without a farmer in domain Y (right)
</div>

<br>

Our training dataset comprises 77,849 images: 32,705 images with the worker for domain X and 45,144 images without the worker for domain Y. 
In addition, to analyze our system qualitatively and quantitatively, we prepared 527 images without a human in the farm 
and created corresponding synthetic images with a human.

※ Currently, our agricultural dataset is not open to the public.

<!--

# Usage

## 1. 

## 2. 

-->

# References
["Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks"](https://arxiv.org/abs/1703.10593)
