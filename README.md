# Unsupervised Grain Kernel Properties Extraction

We need to estimate properties of grains from images to support downstream predictive and physical modeling tasks by other systems on harvesters.  Essentially this is feature extraction, or feature engineering.

Each of the example images are taken the same distance from the glass behind which the grain sits.  On the left is low moisture corn, which generally has small kernels.  On the right we have high moisture corn, which generally has large swollen (larger) kernels.


<img src="Data/NG3_GQ_Corn_11MC_59lbs_50F_2017-11-16_11-0-33_Sensor-1_Frame-36_Ts-1510851850.1548.png" width="400" hspace="10" align="left">  <img src="Data/NG3_GQ_Corn_32MC_53lbs_99F_2017-7-18_10-31-45_Sensor-1_Frame-32_Ts-1500374550.1573.png" width="400" align="right">

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

## Morphological Feature Extraction of Grain and MOG

One approach involves stacking a lot of preprocessing steps followed by fine-tuned/engineered operations such as filters and morphological image processing methods to obtain intuitive features.  The nice part about this approach is that it's fully transparent...i.e. we can "peer inside" the process to see how it's working and ensure we are obtaining the desired features.  For physical modeling tasks this approach is almost required, since deep representation learning approaches cannot guarentee interpretable features.  The results for the high and low moisture images are below. 
<br/><br/>
<img src="Data/high_moisture_corn_labels.png" width="350" hspace="30" align="left">  <img src="Data/high_moisture_overlay.png" width="350" hspace="0" align="right">
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/>
<br/>
And low moisture image........
<br/><br/>
<img src="Data/low_moisture_corn_labels.png" width="350" hspace="30" align="left">  <img src="Data/low_moisture_overlay_corn.png" width="350" hspace="0" align="right">
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/>
<br/>
To obtain physical/interpretable features (e.g. aspect ratio and area).
<br/><br/>
<img src="Data/aspect_ratio.png" width="350" hspace="30" align="left">  <img src="Data/area.png" width="350" hspace="0" align="right">
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/>
<br/>
These results are pretty good, and all without annotated data!! From this we can extract properties like area and aspect ratio, as well as other factors like colors to classify object instances without labels (clustering).
<br/><br/>


## Unsupervised Deep Learning

We can also use generative models to find properties, although the results may not be as intuitive, and the optimization process can be easy to mess up for non-experts in statistics and optimization.  This approach can be very useful for downstream predictive modeling tasks using machine learning though, so long as the dataset we train with is sufficiently representative of the important variations in the dataset.  This point cannot be overemphasized since a naive attempt to apply unsupervised learning here (i.e. one without both theoretical and domain knowledge) will generalize very poorly.  This can include linear methods (PCA) and nonlinear methods (autoencoders and variational autoencoders).
<br/><br/><br/>
** unsuperivsed deep learning part to be added **
