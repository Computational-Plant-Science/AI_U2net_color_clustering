# AI_U2net_color_clustering (SMART branch)

A machine learning model U2net and OpenCV-based color clustering method that performs object segmentation in a single shot

Plant phenotyping using computer vision.

Author: Suxing Liu


##


![Optional Text](../main/media/Smart.png) 

Robust and parameter-free plant image segmentation.

1. Process with plant image top view, including whole tray plant image, this tool will segment it into individual images.

2. Robust segmentation based on parameter-free color clustering method and pre-trained machine learning model U2net.


## Inputs 

   An image file, individual plant tray image from the top view, captured by ANY modern digital camera. 

## Results 

    Segmentation mask and masked foreground image


## Sample Test

![Sample Input](../main/media/IMG_6241.png)

Sample input image: two roots interaction in a meshed box, Designed by [William Alexander Lavoy](https://www.linkedin.com/in/william-lavoy-547775188/) @ wlavoy@arizona.edu, 



![Sample Output: mask](../main/media/IMG_6241_mask.png)

Sample output: mask image

![Sample Output: mask](../main/media/IMG_6241_masked.png)

Sample output: masked foreground image with roots object only


<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Contents**

<!-- END doctoc generated TOC please keep comment here to allow auto-update -->



Input image requirement:

Plant top view image captured by HD resolution RGB camera, prefer a black background with even illumination environment. 

Example input can be downloaded from the "/sample_test/" folder, which contains top-view images of the same Arabidopsis plant from different time points. 





## Usage by cloning the  GitHub repo to local environment

Main pipeline: 

    Default parameters: python3 ai_color_cluster_seg.py -p /$path_to_test_image_folder/ -ft png

    User defined parameters: python3 ai_color_cluster_seg.py -p /$path_to_test_image_folder/ -ft png -o /$path_to_result_folder/ -s lab -c 2 -min 500 -max 1000000 -pl 0


Note: pl can be set to 1 to use parallel processing mode locally using host PC mutiple cores and threads, will consume more memory. 



1. Clone the repo into the local host PC:

```bash

    git clone https://github.com/Computational-Plant-Science/AI_U2net_color_clustering.git

```

   Now you should have a clone of the pipeline source code in your local PC, the folder path was:
```
   /$host_path/AI_U2net_color_clustering/
   
    Note: $host_path can be any path chosen by the user. 
```

2. Prepare your input image folder path,

   here we use the sample images inside the repo as input, the path was:
```
   /$host_path/AI_U2net_color_clustering/sample_test/
```

3. Main pipeline to compute the segmentation results:

```bash

   cd /$host_path/AI_U2net_color_clustering/

   
   python3 /$host_path/AI_U2net_color_clustering/ai_color_cluster_seg.py -p /$host_path/AI_U2net_color_clustering/sample_test/ -ft CR2 -o /$host_path/AI_U2net_color_clustering/sample_test/

```
Results will be generated in the output folder by adding "/$host_path/AI_U2net_color_clustering/sample_test/"

The default input image type png, can be changed by adding a parameter such as " -ft CR2".




## Usage for Docker container 


[Docker](https://www.docker.com/) is suggested to run this project in a Unix environment.

1. Download prebuilt docker container from DockerHub 

```bash

    docker pull computationalplantscience/AI_U2net_color_clustering

    docker run -v /$path_to_test_image:/images -it computationalplantscience/AI_U2net_color_clustering

Note: The "/" at the end of the path was NOT needed when mounting a host directory into a Docker container. Above command mount the local directory "/$path_to_test_image" inside the container path "/images"
Reference: https://docs.docker.com/storage/bind-mounts/
```

For example, to run the sample test inside this repo, under the folder "sample_test", first locate the local path 
```
    docker run -v /$path_to_test_image:/images -it computationalplantscience/AI_U2net_color_clustering
```

    then run the mounted input images inside the container:
``` 
    python3 /opt/code/ai_color_cluster_seg.py -p /images/ -ft CR2 
```
    or 
```
    docker run -v /$path_to_test_images:/images -it computationalplantscience/AI_U2net_color_clustering  python3 /opt/code/ai_color_cluster_seg.py -p /images/ -ft CR2 
```

2. Build your local container

```bash

    docker build -t test_container -f Dockerfile .

    docker run -v  /$path_to_test_images:/images -it test_container

```

3. Addition function to change the image format from 

```bash

    docker build -t test_container -f Dockerfile .

    docker run -v  /$path_to_test_images:/images -it test_container 
    
    python3 image_converter.py -p /images/ -ft CR2  -o /images/
    
    note: "-o /images/" was output path, user can create a new folder such as "/$path_to_test_images/png/" then change output path to "-o /images/png/"
        
    or docker run -v  /$path_to_test_images:/images -it computationalplantscience/AI_U2net_color_clustering python3 image_converter.py -p /images/ -ft CR2  -o /images/

``` 



Results will be generated in the same input folder.

Note: They are processed copies of the original images, all the image content information was processed and extracted as traits information. 






<br/><br/> 




Reference:

    https://arxiv.org/pdf/2005.09007.pdf
    https://github.com/NathanUA/U-2-Net
    https://github.com/pymatting/pymatting
    https://github.com/danielgatis/rembg
    

## Citation
```
@InProceedings{Qin_2020_PR,
title = {U2-Net: Going Deeper with Nested U-Structure for Salient Object Detection},
author = {Qin, Xuebin and Zhang, Zichen and Huang, Chenyang and Dehghan, Masood and Zaiane, Osmar and Jagersand, Martin},
journal = {Pattern Recognition},
volume = {106},
pages = {107404},
year = {2020}
}
```


