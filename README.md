# Unsupervised Grain Kernel Properties Extraction

We need to extract properties from grains to support downstream tasks.  Essentially this is feature extraction.

Let's examine a couple images below.  Each of these images are taken the same distance from the glass behind which the grain sits.  On the left is low moisture corn, which generally has small kernels.  On the right we have high moisture corn, which generally has large swollen (larger) kernels.


<img src="Data/NG3_GQ_Corn_11MC_59lbs_50F_2017-11-16_11-0-33_Sensor-1_Frame-36_Ts-1510851850.1548.png" width="400" hspace="10" align="left">  <img src="Data/NG3_GQ_Corn_32MC_53lbs_99F_2017-7-18_10-31-45_Sensor-1_Frame-32_Ts-1500374550.1573.png" width="400" align="right">

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

## Unsupervised Learning Method #1

Utilizing some more classic computer vision approaches can be time consuming and wrought with pain for the less creative scientists, but also very effective at obtaining intuitive results using very little to no annotated data, which defies most modern deep learning approaches.  Follow the "main" code to obtain segmentation results like so....
<br/><br/>
<img src="Data/high_moisture_corn_labels.png" width="350" hspace="30" align="left">  <img src="Data/high_moisture_overlay.png" width="350" hspace="0" align="right">
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/>
<br/>
And like so........
<br/><br/>
<img src="Data/low_moisture_corn_labels.png" width="350" hspace="30" align="left">  <img src="Data/low_moisture_overlay_corn.png" width="350" hspace="0" align="right">
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/>
<br/>
These results are pretty good, and all without annotated data!! From this we can extract properties like area and aspect ratio, as well as other factors like colors to classify object instances without labels (clustering).
<br/><br/>


## Unsupervised Learning Method #2

We can also use generative models to find properties, although the results may not be as intuitive, and the optimization process can be easy to mess up for non-experts in statistics and optimization.  This can include linear methods (PCA) and nonlinear methods (autoencoders and variational autoencoders).
