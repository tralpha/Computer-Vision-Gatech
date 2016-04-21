#!/usr/bin/python

import numpy as np
import cv2
import matplotlib.pyplot as plt

def show_img(img):
    """
    Shows an image in RGB using matplotlib pyplot

    Args:
        img: An opencv instance of the image to be displayed
    """
    if img.ndim == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        color_map = None
    else:
        color_map = 'gray'
    plt.imshow(img, cmap=color_map)
    #return imgplot


def determine_fig_partition(num_imgs):
    """
    Determines how the pyplot figure will be partitioned, based on the 
    number of images to be displayed. Helper function for the function 
    show_multiple_images.

    Args:
        num_imgs: The number of images to be displayed.
    """
    #print num_imgs
    if num_imgs == 1:
        num_plots_rows = 1
        num_plots_cols = 1
    elif num_imgs == 7:
        num_plots_rows = 2
        num_plots_cols = 4
    elif num_imgs % 2 == 0 and num_imgs >= 2:
        num_plots_rows = num_imgs/2
        num_plots_cols = 2
    elif num_imgs % 3 == 0 and num_imgs >= 3:
        num_plots_rows = num_imgs/3
        num_plots_cols = 3
    elif num_imgs % 5 == 0 and num_imgs >= 5:
        num_plots_rows = num_imgs/5
        num_plots_cols = 5
    return num_plots_rows, num_plots_cols


def show_multiple_images(images, convert_to_rgb = True):
    """
    Displays multiple images in a pyplot figure.

    Args:
        images: A dictionary mapping an image name to the opencv instance of 
        that image.
        convert_to_rgb: A boolean to determine whether you wish to convert to 
        rgb or not.
    """
    num_imgs = len(images)
    num_rows, num_cols = \
                determine_fig_partition(num_imgs)
    
    fig = plt.figure(figsize=(20,10))
    for i,img in enumerate(images, 1):
        a = fig.add_subplot(num_rows, num_cols, i)
        a.set_title(img)
        if convert_to_rgb == True:
            #cv2.cvtColor(images[img], cv2.COLOR_BGR2RGB)
            #plt.imshow(cv2.cvtColor(images[img],\
             #                                 cv2.COLOR_BGR2RGB))
            show_img(images[img])
        else:
            #plt.imshow(images[img])
            show_img(images[img])
        a.get_xaxis().set_ticks([])
        a.get_yaxis().set_ticks([])  
    plt.show()


def determine_img_center(img, center_left=True, center_up=True, center=100):
    """
    Determines the center of an image.

    Args:
        img: An opencv instance of an image.
        center_left: A boolean to determine whether the you should push the 
            center width to the left or push it to the right. If the value 
            is true, the value will be pushed to the left. If it is false, 
            then it will be pushed to the right.
        center_up: A boolean to determine whether the you should push the 
            center of the image height to the up or down. If the value is true, 
            the value will be pushed to up. If it is false, then it will be 
            pushed down.

    Returns:
        A tuple, representing the center of the image height and the center of 
        the image width.
    """
    if img.shape[0] % 2 == 0:
        center_height = img.shape[0]/2
    elif center_up == True:
        center_height = img.shape[0]-1/2
    else:
        center_height = img.shape[0]+1/2

    if img.shape[1] % 2 == 0:
        center_width = img.shape[1]/2
        even_height = True
    elif center_left == True:
        center_width = img.shape[1]-1/2
    else:
        center_width = img.shape[1]+1/2
    half_center = center/2
    first_dim_idx = center_height-half_center, center_height+half_center
    sec_dim_idx = center_width-half_center, center_width+half_center
    return first_dim_idx, sec_dim_idx


def center_100_pixels(img, center_left=True, center_up=True, center=100):
    """
    Extracts the middle 100 pixels of an image.

    Args:
        img: An opencv instance of an images.
        center_left: A boolean to determine whether the you should push the 
            center width to the left or push it to the right. If the value 
            is true, the value will be pushed to the left. If it is false, 
            then it will be pushed to the right.
        center_up: A boolean to determine whether the you should push the 
            center of the image height to the up or down. If the value is true, 
            the value will be pushed to up. If it is false, then it will be 
            pushed down.
        center: An int to indicate how many middle pixels you need to extract.

    Returns:
        A tuple, representing the center of the image height and the center of
        the image width.

    """
    center_height = 0
    center_width = 0
    even_height = False
    first_dim, sec_dim = determine_img_center(img)
    center_pixs = img[first_dim[0]:first_dim[1], sec_dim[0]:sec_dim[1]]
    #import ipdb; ipdb.set_trace()
    return center_pixs


def replace_100_pix(img_1, img_2, center=100):
    img_3 = img_2
    img_1_center = center_100_pixels(img_1)
    img_3_first, img_3_sec = determine_img_center(img_3)
    img_3[img_3_first[0]:img_3_first[1], img_3_sec[0]:img_3_sec[1]] =\
                                                             img_1_center
    return img_3


def shift_img(img):
    """
    Shifts image by 2 pixels to the left
    Args:
        img: An opencv instance of the image.

    Returns:
        An opencv instance of the shifted image.
    """
    shifted = np.roll(img, -2, axis=1)
    if img.ndim == 3:
        shifted[:,-2:,:] = 0
    else:
        shifted[:,-2:] = 0
    return shifted


def conv_to_uint8(arr):
    """
    Converts an array type to uint8 suitable for image processing.
    Args:
        array: A numpy array
    Returns:
        A uint8 numpy array
    """
    uint8_arr = np.uint8(np.clip(arr, 0, 255))
    return uint8_arr
    



if __name__ == '__main__':
    center_100_pixels()





