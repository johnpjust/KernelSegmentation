# KernelSegmentation

We need to extract properties from grains to support downstream tasks.  Essentially this is feature extraction, but the end users want intuition about the features so we can't just use the old "bag-'o-features" trick.

Let's examine a couple images below.  Each of these images are taken the same distance from the glass behind which the grain sits.  On the left is low moisture corn, which generally has small kernels.  On the right we have high moisture corn, which generally has large swollen (larger) kernels.


<img src="Data/NG3_GQ_Corn_11MC_59lbs_50F_2017-11-16_11-0-33_Sensor-1_Frame-36_Ts-1510851850.1548.png" width="400" hspace="20">  <img src="Data/NG3_GQ_Corn_32MC_53lbs_99F_2017-7-18_10-31-45_Sensor-1_Frame-32_Ts-1500374550.1573.png" width="400">

## Lighting Corrections
As a side note, while these images conveniently have color bands to support color corrections for different bulb outputs to maintain unit to unit consistency, we're going to ignore that for now and absorb that kind of variability into the algorithm since we don't even know for sure how reliable those bands are.  Next we trim the images and deal with non-uniform lighting.  Here we remind that most real-world images do not have uniform lighting throughout the images, which is one of the fundamental things that makes generalizing image processing algorithms difficult.  The signal (light) is not uniform and constant within and between images.  In this case, the corners/edges of the window are darker than the middle, which can cause a lot of issues with segmentation.  To deal with this, we will apply a Gaussian filter on the image to find overall lighting intensities and subtract it off the original image.




While the difference is subtle to our eyes, it can make a big difference with some of the algorithms we're about to use.
