#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
import os
from classifier import classifier 
# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
#  

def classify_images(images_dir, results_dic, model):
    
    """
    Creates classifier labels with the classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. The classifier
    labels are formatted to match the pet image labels by converting them to lowercase
    and stripping leading and trailing whitespace.
    
    Parameters:
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                    index 0 = pet image label (string)
                    --- where index 1 & index 2 are added by this function ---
                    NEW - index 1 = classifier label (string)
                    NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                                      and classifier labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet, alexnet, vgg (string)
     Returns:
           None - results_dic is a mutable data type so no return needed.         
    """
# Iterate over each image in the directory
    for filename in os.listdir(images_dir):
        # Check if the file is an image file
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Extract the pet image label from the filename
            pet_label = filename.lower().split("_")
            pet_label = " ".join(pet_label[:-1])  # Remove the file extension
            pet_label = pet_label.strip()

            # Call the classifier function to get the classifier label
            classifier_label = classifier(os.path.join(images_dir, filename), model)

            # Format the classifier label to match the pet image label
            classifier_label = classifier_label.lower().strip()

            if (pet_label in classifier_label):
                match=1
    # code here checks if pet_label is present in classifier_label
            else:
                match=0
            

            # Add the classifier label and match indicator to the results_dic
            results_dic[filename].extend([classifier_label, match])
    