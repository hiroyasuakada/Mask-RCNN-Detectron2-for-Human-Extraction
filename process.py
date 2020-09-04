import torch, torchvision
print(torch.__version__)

import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import cv2
import random
import os, glob
import sys
import threading

# import some common detectron2 utilities
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer as FullVisualizer
from detectron2_repo_with_revision.detectron2.utils.visualizer import Visualizer as MaskVisualizer
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import ColorMode


class MaskRCNN(object):
    def __init__(self):
        # load mask-structure
        self.cfg = get_cfg()
        self.cfg.merge_from_file(
            "./detectron2_repo_with_revision/configs/Misc/cascade_mask_rcnn_X_152_32x8d_FPN_IN5k_gn_dconv.yaml")
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
        self.cfg.MODEL.WEIGHTS = \
            "./detectron2_repo_with_revision/configs/model/cascade_mask_rcnn_X_152_32x8d_FPN_IN5k_gn_dconv.pkl"
        self.predictor = DefaultPredictor(self.cfg)

        # set params for binary mask
        self.threshold = 0.0000000001

        # set threading
        self.lock = threading.Lock()

    def main(self):
        # create dir for outputs
        self.mkdir()

        # get file path in directory
        file_path = './input_image/*.jpg'
        files = glob.glob(file_path)

        for file in files:
            img = cv2.imread(file)
            outputs = self.predictor(img)
            output_name = os.path.basename(file)

            self.full_prediction(img, outputs, output_name)
            self.mask_prediction(img, outputs, output_name)
            self.binary_mask_prediction(img, outputs, output_name)

            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

    def full_prediction(self, img, outputs, output_name):
        v_full = FullVisualizer(img[:, :, ::-1], MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]), scale=1.0)
        v_full = v_full.draw_instance_predictions(outputs["instances"].to("cpu"))
        output_folder_path = "./output_image/image_with_full_prediction/{}".format(output_name)
        cv2.imwrite(output_folder_path, v_full.get_image()[:, :, ::-1])

    def mask_prediction(self, img, outputs, output_name):
        v_mask = MaskVisualizer(img[:, :, ::-1], MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]),
                                scale=1.0, instance_mode=ColorMode.SEGMENTATION)
        v_mask, is_in_person = v_mask.draw_instance_predictions(outputs["instances"].to("cpu"), output_name)

        if is_in_person == 1:
            output_folder_path = "./output_image/image_with_mask_cropped/{}".format(output_name)
            cv2.imwrite(output_folder_path, v_mask.get_image()[:, :, ::-1])

        elif is_in_person == -1:
            print('{} is disregarded due to no finding of figure'.format(output_name))

    def binary_mask_prediction(self, img, outputs, output_name):
        mask_base = np.zeros((img.shape[0], img.shape[1], img.shape[2]), np.uint8)
        v_binary_mask = MaskVisualizer(mask_base, MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]),
                                       scale=1.0, instance_mode=ColorMode.SEGMENTATION)
        v_binary_mask, is_in_person = v_binary_mask.draw_instance_predictions(outputs["instances"].to("cpu"), output_name)

        if is_in_person == 1:
            v_mask_gray = cv2.cvtColor(v_binary_mask.get_image()[:, :, ::-1], cv2.COLOR_RGB2GRAY)
            ret, v_binary_mask_thresh = cv2.threshold(v_mask_gray, self.threshold, 255, cv2.THRESH_BINARY)
            # cv2.imshow('output_image/binary_mask', v_binary_mask_thresh)
            output_binary_mask_folder_path = "./output_image/binary_mask/{}".format(output_name)
            cv2.imwrite(output_binary_mask_folder_path, v_binary_mask_thresh)

            img_mask = cv2.cvtColor(v_binary_mask_thresh, cv2.COLOR_GRAY2RGB)
            img_with_mask = cv2.bitwise_and(img, img_mask)
            output_mask_folder_path = "./output_image/cropped_figure/{}".format(output_name)
            cv2.imwrite(output_mask_folder_path, img_with_mask)

        elif is_in_person == -1:
            print('{} is disregarded due to no finding of figure'.format(output_name))

    def mkdir(self):
        # check if output folders exist or not
        if not os.path.exists('./output_image'):
            os.mkdir('./output_image')
        if not os.path.exists('./output_image/image_with_full_prediction'):
            os.mkdir('./output_image/image_with_full_prediction')
        if not os.path.exists('./output_image/image_with_mask_cropped'):
            os.mkdir('./output_image/image_with_mask_cropped')
        if not os.path.exists('./output_image/binary_mask'):
            os.mkdir('./output_image/binary_mask')
        if not os.path.exists('./output_image/cropped_figure'):
            os.mkdir('./output_image/cropped_figure')


if __name__ == '__main__':
    mask = MaskRCNN()
    mask.main()






