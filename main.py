import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from skimage import io, filters, color, morphology, feature, exposure, util, measure
# from skimage import filters
# from skimage import color
import PIL.Image
import PIL
from scipy import ndimage as ndi
import cv2
cmap = matplotlib.colors.ListedColormap (np.random.rand ( 256,3))

img = io.imread(r'D:\Matlab\GrainParticleSize\NG3_GQ_Corn_11MC_59lbs_50F_2017-11-16_11-0-33_Sensor-1_Frame-36_Ts-1510851850.1548.png')
# img = io.imread(r'D:\Matlab\GrainParticleSize\NG3_GQ_Corn_32MC_53lbs_99F_2017-7-18_10-31-45_Sensor-1_Frame-32_Ts-1500374550.1573.png')

img = img/255.;
x1 = 63;x2 = x1+597;y1 = 21;y2 = y1+439;
imgc_ = img[y1:y2, x1:x2]
# imgc = imgc_
background = filters.gaussian(color.rgb2gray(imgc_), 60)
imgc = imgc_-np.expand_dims(background, axis=2);imgc = np.minimum(imgc - np.min(imgc),1);

## possibly use adaptive histogram before otsu to enhance contrast and get markers isolated easily (w/o distance transform)
## could do this after finding sure foreground as well so that we can ensure the watershed is only used to separate the kernels
# imgca = exposure.equalize_adapthist(imgc)

## sure background
se = morphology.disk(20);
Ie = morphology.erosion(color.rgb2gray(imgc),se);
Iobr = morphology.reconstruction(Ie,color.rgb2gray(imgc))
thresh = filters.threshold_otsu(Iobr)
bg = imgc > thresh;
bg = bg.astype(np.float)
# plt.figure();plt.imshow(np.max(bg, axis=2))
# plt.title('Opening-by-Reconstruction')

## subtract off gradient lines from sure_bg then find markers
sure_bg=np.max(bg, axis=2)
gradlines = feature.canny(color.rgb2gray(imgc), 4)
D1 = ndi.distance_transform_edt(np.maximum(sure_bg-gradlines,0))
dist_binary1 = D1 > 5
dist_binary1 = dist_binary1.astype(np.float)
# plt.figure();plt.imshow(dist_binary1)
dist_binary1_ = morphology.remove_small_holes(util.pad(dist_binary1, (1,), 'constant', constant_values=0).astype(np.int), 400)
dist_binary1_ = dist_binary1_[1:-1, 1:-1]
# plt.figure();plt.imshow(dist_binary1_)
## sure foreground (use only 2nd and 3rd channels and find markers)
fat_markers=bg[:,:,1]
D2 = ndi.distance_transform_edt(fat_markers)
dist_binary2 = D2 > 5
dist_binary2 = dist_binary2.astype(np.float)
# plt.figure();plt.imshow(dist_binary2)
dist_binary2_ = morphology.remove_small_holes(util.pad(dist_binary2, (1,), 'constant', constant_values=0).astype(np.int), 300)
dist_binary2_ = dist_binary2_[1:-1, 1:-1]
# plt.figure();plt.imshow(dist_binary2_)

sure_fg=dist_binary1_.astype(np.float) * dist_binary2_.astype(np.float)

sure_fgo = morphology.binary_opening(sure_fg, morphology.disk(5))

unknown = np.maximum(sure_bg-sure_fgo,0)

markers = measure.label(sure_fgo, background=0)
markers += 1
markers[unknown==1] = 0
# plt.figure();plt.imshow(markers, cmap=cmap)

imgc_ = np.uint8(imgc*255.)
labels = cv2.watershed(imgc_,markers)

plt.figure();plt.imshow(labels.get(), cmap=cmap)
imgc_overlay = imgc
imgc_overlay[labels.get() == -1] = [1,0,0]
#######################################################################
