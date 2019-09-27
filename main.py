import numpy as np
import matplotlib.pyplot as plt
from skimage import io, filters, color, morphology
# from skimage import filters
# from skimage import color
import PIL.Image
import PIL

img = io.imread(r'D:\Matlab\GrainParticleSize\NG3_GQ_Corn_11MC_59lbs_50F_2017-11-16_11-0-33_Sensor-1_Frame-36_Ts-1510851850.1548.png')
img = img/255.;
# img = skimage.io.imread(r'D:\Matlab\GrainParticleSize\NG3_GQ_Corn_32MC_53lbs_99F_2017-7-18_10-31-45_Sensor-1_Frame-32_Ts-1500374550.1573.png')
x1 = 63;x2 = x1+597;y1 = 21;y2 = y1+439;
imgc = img[y1:y2, x1:x2]

## possibly use adaptive histogram before this to enhance contrast

## this segmented the image almost completely with red lines around the kernels
thresh = filters.threshold_otsu(color.rgb2gray(imgc))
binary_ = imgc > thresh;
binary3 = binary_.astype(np.float)
plt.imshow(binary3) ## not sure what happened here, but red lines around the kernels segmented everything????

plt.figure();plt.imshow(binary3[:,:,1]) ## very, very close to having all the markers isolated
plt.figure();plt.imshow(binary3[:,:,0]) ## this is the full mask which shows the sure foreground and background, but without the objects separated

binary_groups = (binary3 == [1,0,0]).astype(np.float)

plt.figure();plt.imshow(binary_groups) ## this will give the

bw = color.rgb2gray(binary)

# background = filters.gaussian(color.rgb2gray(imgc), 60)
# J = double(Irs)-double(background);J = uint8(J - min(J(:)));

plt.figure();plt.imshow(skimage.exposure.equalize_adapthist(imgc, kernel_size=25, clip_limit=0.01))