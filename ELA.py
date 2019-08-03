from PIL import Image, ImageChops
import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
import glob
from PIL import Image
import os
from pylab import *
import re
from PIL import Image, ImageChops, ImageEnhance


def convert_to_ela_image(path, quality):
    filename = path
    resaved_filename = filename.split('.')[0] + '.resaved.jpg'
    ELA_filename = filename.split('.')[0] + '.ela.png'
    
    im = Image.open(filename).convert('RGB')
    im.save(resaved_filename, 'JPEG', quality=quality)
    resaved_im = Image.open(resaved_filename)
    
    ela_im = ImageChops.difference(im, resaved_im)
    
    extrema = ela_im.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff
    ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)
    return ela_im


#convert_to_ela_image("I:\\casia-dataset\\Train\\Train real\\Au_ani_00001.jpg",90)
final_image = []
import glob, os
os.chdir("I://casia-dataset//Train//Real")
for file in glob.glob("*.tif"):
    image = convert_to_ela_image(file,90)
    final_image.append(image)

print(len(final_image))

outpath ="I:\\casia-dataset\\Train\\ELA Fake\\"
idx = 2065
for i in range(len(final_image)):
    print(i)
    img = final_image[i]
    open_cv_image = np.array(img)
    cv2.imwrite(outpath + str(idx) + '.jpg', open_cv_image)
    idx = idx + 1