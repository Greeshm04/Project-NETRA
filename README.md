# Project Netra 

Project NETRA is Targeting Satellite Imaginary .
The Main Work is to Detect Change and Extract Features from given Satellite imaginary.

## Change Detection

* Used Computer Vision Techniques and own Image Pre-Processing Techniques for Better Results.
* We are getting change from each pixel.
* For Image Pre Processing and clearing noise we have used 20x20 Pixel Matrix and Clearing Changes which are below 20% for better accuracy. 

## Feature Extraction

* Used Mask RCNN Weights Provided by Detectron2 (a Facebook’s Open Source Platform for Develop further).
* We have made our Custom Polygon Dataset of Satellite Imaginary from Google Earth.
* We have Trained 19+ Models out of which we have selected one Model in which we are getting 90+ accuracy.

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
