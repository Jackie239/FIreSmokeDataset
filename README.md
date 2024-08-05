# Fire and smoke datasets

fire and smoke object detection datasets in pascal format

## D-Fire

offical dataset: https://github.com/gaiasd/DFireDataset  
offical one is coco format and **some annotations are wrong**  

processed dataset: https://pan.baidu.com/s/1-zAn5jfAgvRWS-POR5tsIQ?pwd=v72u  
processed one is pascal format  
wrong annotations are deleted, this dataset is safe to use

### generate dataset

generate pascal format from offical format with tools in './D-Fire/jupyter/'

## Flame

offical dataset: https://github.com/AlirezaShamsoshoara/Fire-Detection-UAV-Aerial-Image-Classification-Segmentation-UnmannedAerialVehicle  
offical one is used for image classification and image segmentation

processed dataset: https://pan.baidu.com/s/1haWZ_RjBHnpF5rSlZ-HLOg?pwd=ndwg  
processed one is pascal format  
bounding boxes are generated from mask

### generate dataset

generate pascal format from offical format with tools in './flame/jupyter/'

## WildFire-Smoke-Dataset-Tensorflow

offical dataset: https://www.kaggle.com/datasets/ahemateja19bec1025/wildfiresmokedataset   
processed dataset: https://pan.baidu.com/s/17zjEjNRNnnfdd0b5ogs9aA?pwd=ctve     
processed one is pascal format    

### generate dataset

generate pascal format from offical format with tools in './WildFire-Smoke-Dataset-Tensorflow/jupyter/'

## Distribution

|dataset|images|smoke boxes|fire boxes|
|:---:|:---:|:---:|:---:|
|D-Fire|11689|11854|14685|
|flame|2003||8779|
|wildFire-smoke|14429|12591|23464|

