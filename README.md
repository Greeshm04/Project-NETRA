# Project Netra 

Project NETRA is a System Developed for Satellite Imaginary Image Processing.
The Main Work is to Detect Change and Extract Features from given Satellite imaginary.

## Change Detection

* Used Computer Vision AI and own Image Pre-Processing Techniques for Better Results.
* We are getting change from each pixel (Comparing each pixel of Both Images).
* For Image Pre-Processing and clearing the noise, we have used 20x20 Pixel Matrix and it Clears Changes that are below 20% Match, for better accuracy. 

## Feature Extraction

* Used Mask RCNN Weights Provided by Detectron2 (Facebook’s Open Source AI Platform for Developers).
* We have made our Custom Polygon Dataset of Satellite Imaginary from Google Earth.
* We have Trained 19+ Models out of we have selected one Model in which we are getting 90+ accuracy.

## Object Detection Model Structure:

* http://ethereon.github.io/netscope/#/gist/db945b393d40bfa26006

## Requirement

* Pytorch: 1.5.1
* Python:3.6+
* Torchvision:0.6.1

## Installation

* pip install python3
* pip install django
* pip install opencv-python
* pip install cython
* python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/index.html
### For CPU:
* pip install torch==1.5.1+cpu torchvision==0.6.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
### For GPU:
* pip install torch==1.5.1 torchvision==0.6.1 -f  https://download.pytorch.org/whl/torch_stable.html

## Time Analysis :

| Hardware      | Change Detection | Object Detection  |
| ------------- |:-------------:| :-----:|
| CPU      | ~ 13 Seconds | ~ 12 Seconds |
| Local GPU      | ~ 13 Seconds      |   ~ 1 Seconds |
| Cloud GPU | -      |    ~ 7 Seconds |


## Sample Output
Before Image

<img src="https://user-images.githubusercontent.com/32408194/92439463-84ae7380-f1c8-11ea-93de-15ec691d8798.jpg" width=680 height=470/>    

After Image

<img src="https://user-images.githubusercontent.com/32408194/92439466-85dfa080-f1c8-11ea-96c6-fc2323b157e3.jpg" width=680 height=470/>

#### Change Detection : (Red Part)

<img src="https://user-images.githubusercontent.com/32408194/92439469-8841fa80-f1c8-11ea-89f2-e643df1fb6b3.png" width=680 height=470/>

#### Feature Detection From Changed Area :

* Blue Shade = Water

* Yellow Shade = Buildings

<img src="https://user-images.githubusercontent.com/32408194/92439472-88da9100-f1c8-11ea-8ae3-cc83ececd8cb.png" width=680 height=470/>


#### Feature Extraction :
Target Image :

<img src="https://user-images.githubusercontent.com/32408194/92439466-85dfa080-f1c8-11ea-96c6-fc2323b157e3.jpg" width=680 height=470/>

Result :

<img src="https://user-images.githubusercontent.com/32408194/92440591-5df13c80-f1ca-11ea-9d77-f4065d0d4700.png" width=680 height=470/>

#### Check /Output Directory For More Results

