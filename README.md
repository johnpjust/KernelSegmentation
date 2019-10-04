# Unsupervised Grain Kernel Properties Extraction

We need to extract properties from grains to support downstream tasks.  Essentially this is feature extraction, but the end users want intuition about the features so we can't just use the old "bag-'o-features" trick.

Let's examine a couple images below.  Each of these images are taken the same distance from the glass behind which the grain sits.  On the left is low moisture corn, which generally has small kernels.  On the right we have high moisture corn, which generally has large swollen (larger) kernels.


<img src="Data/NG3_GQ_Corn_11MC_59lbs_50F_2017-11-16_11-0-33_Sensor-1_Frame-36_Ts-1510851850.1548.png" width="400" hspace="20">  <img src="Data/NG3_GQ_Corn_32MC_53lbs_99F_2017-7-18_10-31-45_Sensor-1_Frame-32_Ts-1500374550.1573.png" width="400">



