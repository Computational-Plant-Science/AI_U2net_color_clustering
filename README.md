# AI_U2net_color_clustering (SMART branch)

A machine learning model U2net and opencv based color clsutering method hat performs object segmentation in a single shot

Plant phenotyping using computer vision.

Author: Suxing Liu


##


![Optional Text](../master/media/Smart.png) 

Robust and parameter-free plant image segmentation.

1. Process with plant image top view, including whole tray plant image, this tool will segment it into individual images.

2. Robust segmentation based on parameter-free color clustering method and pre-trained machine learning model U2net.


## Inputs 

   Image file, individual plant tray image from top view, captured by ANY modern digital camera. 

## Results 

    Segmentation mask and masked foreground image


## Sample workflow

![Sample Input](../master/media/IMG_6241.png)

![Sample Output: mask](../master/media/IMG_6241_mask.png)

![Sample Output: mask](../master/media/IMG_6241_masked.png)



<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Contents**

<!-- END doctoc generated TOC please keep comment here to allow auto-update -->








## Usage in the local environment by cloning the whole GitHub repo 




Input image requirement:

Plant top view image captured by HD resolution RGB camera, prefer a black background with even illumination environment. 

Example input can be downloaded from the "/sample_test/" folder, which contains top-view images of the same Arabidopsis plant from different time points. 


1. Download the repo into the local host PC:

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

2. extract traits:

```bash

   cd /$host_path/SMART/

   
   python3 /opt/AI_U2net_color_clustering/core/ai_color_cluster_seg.py -p /$host_path/AI_U2net_color_clustering/sample_test/ -ft png -o /$host_path/AI_U2net_color_clustering/sample_test/

```
Results will be generated in the output folder by adding "/$host_path/AI_U2net_color_clustering/sample_test/"

The default input image type png, can be changed by adding a parameter such as " -ft png".




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
    docker run -v /$path_to_AI_U2net_color_clustering_repo/AI_U2net_color_clustering/sample_test:/images -it computationalplantscience/AI_U2net_color_clustering
```

    then run the mounted input images inside the container:
``` 
    python3 /opt/smart/core/ai_color_cluster_seg.py -p /images/ -ft png 
```
    or 
```
    docker run -v /$path_to_AI_U2net_color_clustering_repo/AI_U2net_color_clustering/sample_test:/images -it computationalplantscience/AI_U2net_color_clustering  python3 /opt/AI_U2net_color_clustering/core/ai_color_cluster_seg.py -p /images/ -ft png
```

2. Build your local container

```bash

    docker build -t smart_container -f Dockerfile .

    docker run -v  /home/suxing/AI_U2net_color_clustering/sample_test:/images -it smart_container

```

Results will be generated in the same input folder.

Note: They are processed copies of the original images, all the image content information was processed and extracted as traits information. 


## Collaboration


The SMART pipeline has been integrated into CyVerse cloud computing-based website: PlantIT (https://plantit.cyverse.org/)

CyVerse users can upload data and run the SMART pipeline for free. 


The SMART pipeline has also been applied in collaboration with following research institutes and companies: 

1. Dr. David G. Mendoza-Cozatl at [University of Missouri](https://cafnr.missouri.edu/person/david-mendoza-cozatl/)

2. Dr. Kranthi Varala at [Purdue University](https://www.purdue.edu/gradschool/pulse/groups/profiles/faculty/varala.html) 

3. Dr. Filipe Matias at [Syngenta](https://www.linkedin.com/in/filipe-matias-27bab5199/)

4. Dr. Tara Enders at [Hofstra University](https://sites.google.com/view/enders-lab/people?pli=1)

5. Briony Parker at [Rothamsted Research](https://repository.rothamsted.ac.uk/staff/98225/briony-parker)

6. Dr. Fiona L. Goggin at [University of Arkansas](https://enpl.uark.edu/people/faculty/uid/fgoggin/name/Fiona+Goggin/)


<br/><br/> 


## Imaging protocol for SMART


![Optional Text](../master/media/plant.jpg)

Setting up plants

    1. Place one plant in one tray.
    2. Use black color mesh to cover the soil.
    3. Place the maker object on the left corner of the tray.
    4. Prefer the plant did not grow out of the boundaries of the tray.




![Optional Text](../master/media/camera.jpg)

Setting up camera

    1. The camera lens should be parallel to the plant surface to capture an undistorted top view. 
    2. The plant object should be in the center of the image and within the focus of the camera lens.
    3. The depth of field should cover the different layers of the plant leaves. 
    4. Higher resolution (e.g., an 8-megapixel camera produces a file size that is 2448 x 3264 PPI) is suggested to acquire clear and sharp image data.



Setting up the lighting environment

    1. Diffuse lighting is suggested. 
    2. Reduce shadow as much as possible.
    3. Keep the illumination environment constant between imaging different plants. 
    4. Avoid overexposure and reflection effects.


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


