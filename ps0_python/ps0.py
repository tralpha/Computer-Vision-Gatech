#!/usr/bin/python

def show_img(img):
    """
    Shows an image in RGB using matplotlib pyplot

    Args:
        img: An opencv instance of the image to be displayed
    """
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)


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
            imgplot = plt.imshow(cv2.cvtColor(images[img],\
                                              cv2.COLOR_BGR2RGB))
        else:
            imgplot = plt.imshow(images[img])
        a.get_xaxis().set_ticks([])
        a.get_yaxis().set_ticks([])  
    plt.show()
