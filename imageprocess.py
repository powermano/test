from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

path = 'E:/valdata1/images/'
out = 'E:/grayvaldata/images/'
files = os.listdir(path)
for filename in files:
    filepath = os.path.join(path, filename)
    img = Image.open(filepath).convert('L')
    outpath = os.path.join(out, filename)
    img.save(outpath)




# img = Image.open('E:/000001.jpg').convert('L')
#
# # plt.imshow(img, cmap='Greys_r')
# # plt.show()
# img.show()
# #img.save('E:/new.jpg')
# a= np.array(img)
# result = cv2.blur(a, (3,3))
# plt.imshow(result,cmap='gray')
# plt.show()
