'''
Name: image_converter.py

Version: 1.0

Summary: Image format conversion from CR2 to png in batch processing mode
    
Author: Suxing Liu

Author-email: suxingliu@gmail.com

Created: 2023-06-05

USAGE:

    python3 image_converter.py -p ~/example/CR2/ -ft CR2  -o ~/example/png/

PARAMETERS:
    ("-p", "--path", dest = "path", type = str, required = True,    help = "path to image file")
    ("-ft", "--filetype", dest = "filetype", type = str, required = False, default='jpg,png', help = "Image filetype")
    ("-o", "--output_path", dest = "output_path", type = str, required = False,    help = "result path")

INPUT:
    Image file in CR2 format

OUTPUT:
    Image file with same name in png format


'''




# import the necessary packages
import os
import glob
import pathlib
from pathlib import Path

import PIL
from PIL import Image

import numpy as np
import argparse
import cv2






# generate folder to store the output results
def mkdir(path):
    # remove space at the beginning
    path=path.strip()
    # remove slash at the end
    path=path.rstrip("\\")
 
    # path exist?   # True  # False
    isExists=os.path.exists(path)
 
    # process
    if not isExists:
        # construct the path and folder
        #print path + ' folder constructed!'
        # make dir
        os.makedirs(path)
        return True
    else:
        # if exists, return 
        
        print ("{} path exists!\n".format(path))
        return False
        


# compute all the traits
def format_converter(image_file):


    ################################################################################
    # load image data
    pil_img = Image.open(image_file)

    cv2_img_arr = np.array(pil_img)

    image = cv2.cvtColor(cv2_img_arr, cv2.COLOR_RGB2BGR)

    return image
        


# get file information from the file path using python3
def get_file_info(file_full_path):
    
    p = pathlib.Path(file_full_path)

    filename = p.name

    basename = p.stem

    file_path = p.parent.absolute()

    file_path = os.path.join(file_path, '')
    
    return file_path, filename, basename



# save result files
def write_file(imagearray, result_path, base_name, ext):

    # save segmentation result
    result_file = (result_path + base_name + ext)
    
    #print(result_file)
    
    cv2.imwrite(result_file, imagearray)
    
    # check saved file
    if os.path.exists(result_file):
        print("Result file was saved at {0}\n".format(result_file))

    else:
        print("Result file writing failed!\n")
    




if __name__ == '__main__':
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", dest = "path", type = str, required = True,    help = "path to image file")
    ap.add_argument("-ft", "--filetype", dest = "filetype", type = str, required = False, default='jpg,png', help = "Image filetype")
    ap.add_argument("-o", "--output_path", dest = "output_path", type = str, required = False,    help = "result path")
    args = vars(ap.parse_args())
    



    # setup input and output file paths

    file_path = args["path"]
    ext = args['filetype']

    #accquire image file list
    filetype = '*.' + ext
    image_file_path = file_path + filetype
    
    #accquire image file list
    imgList = sorted(glob.glob(image_file_path))

    # save folder construction
    if (args['output_path']):
        result_path = args['output_path']
    else:
        # result folder construction
        mkpath = os.path.dirname(file_path) + '/png'
        mkdir(mkpath)
        result_path = mkpath

    # result file path
    #result_path = args["output_path"] if args["output_path"] is not None else file_path

    result_path = os.path.join(result_path, '')
    
    # print out result path
    print("results_folder: {}\n".format(result_path))



    #########################################################################
    # scan the folder to remove the 0 size image
    for image_id, image_file in enumerate(imgList):
        try:
            image = Image.open(image_file)
        except PIL.UnidentifiedImageError as e:
            print(f"Error in file {image_file}: {e}")
            os.remove(image_file)
            print(f"Removed file {image_file}")

    ############################################################################
    #accquire image file list after remove error images
    imgList = sorted(glob.glob(image_file_path))

    #########################################################################
    # pipeline
    #loop execute
    for image_id, image_file in enumerate(imgList):

        (file_path, filename, basename) = get_file_info(image_file)

        print("Convert the format of input image file {} ...\n".format(filename))

        # main pipeline to perform the image format conversion from raw cr2 to png
        image_png = format_converter(image_file)

        # save result image as png format, note can be any format by changing the '.png' to '.jpg' etc..
        write_file(image_png, result_path, basename,'.png')


        
        
        




    

    
