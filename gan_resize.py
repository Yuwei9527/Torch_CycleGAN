# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 13:08:50 2021

@author: aiuser
"""

import os
import cv2

org  = 'C:/Users/aiuser/Desktop/lai/pytorch-CycleGAN-and-pix2pix-master/Pineapple_backup/ROI/Defect/'
root = 'C:/Users/aiuser/Desktop/lai/pytorch-CycleGAN-and-pix2pix-master/result_path_exp2/'

save_dir = 'C:/Users/aiuser/Desktop/lai/pytorch-CycleGAN-and-pix2pix-master/1_GAN_resize_path/exp2/'
path = os.listdir(org)

for i in range(0, len(path)):
    img = cv2.imread(root+path[i]) # GAN_DEFECT
    
    img_org = cv2.imread(org+path[i]) # DEFECT FREE
    
    w, h, _ = img_org.shape
    
    resized_img = cv2.resize(img, (h, w))
    
    w1, h1, _ = resized_img.shape
    
    cv2.imwrite(save_dir+path[i], resized_img)