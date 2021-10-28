# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:36:01 2021

@author: aiuser
"""  
#%%
#2021/1026 for dcgan
import os
from PIL import Image
import random

save_dir = 'C:/Users/aiuser/Desktop/lai/DCGAN-PyTorch-master/exp_2/inference_result_rm_bg_paste_BG/'     
root_img = 'C:/Users/aiuser/Desktop/lai/pytorch-CycleGAN-and-pix2pix-master/Pineapple_backup/ROI/Defect/'
root_mask = 'C:/Users/aiuser/Desktop/lai/DCGAN-PyTorch-master/exp_2/inference_result_rm_bg/'
model_names = os.listdir(root_mask)

#https://blog.csdn.net/lly1122334/article/details/107979207
#2021/10/27 修正圖片只能去被而無法直接貼上的問題
for k in range(1, 101):
    for model in model_names:
        temp1 = os.listdir(root_mask+'/'+model)
        temp2 = os.listdir(root_img)
        random.shuffle(temp2)
        temp2 = temp2[:382]
        
        for i in range(0, len(temp1)):
            img = Image.open(root_img+temp2[i]).convert('RGBA') # BG
            img = img.resize((64, 64))
            img_copy = img.copy()

            
#            print(img.size)
            
            img2 = Image.open(root_mask+'/'+model+'/'+temp1[i]).convert('RGBA') # 20210625_fixed # fake_Defect
            img2 = img2.resize((64, 64)) 
#            print(img2.mode)
        
            # Transparency
            newImage = []
            for item in img2.getdata():
                if item[:3] == (0, 0, 0):
                    newImage.append((0, 0, 0, 0))
                else:
                    newImage.append(item)
            
            img2.putdata(newImage)
        
            img_copy.paste(img2, img2)
            temp = save_dir+'/'+model
            os.makedirs(temp, exist_ok=True)  
#            img.show()
            img_copy.save(temp+'/'+temp1[i])
