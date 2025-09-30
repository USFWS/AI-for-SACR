import pandas as pd
import os
import shutil

# The script searches a image directory and copies/moves images that are listed in a csv file
# the csv file should have column labeled as "unique_image_jpg"

# Data inputs:
# csv data= list of images to be copied/moved (column header of 'unique_image_jpg')
# root_dir = directory of images to search
# dest1 = destination folder to move/copy images into

#image_dir = "D:/SACR_models/SACR_FIX/survey_images_2025/"
#csv_data = pd.read_csv("D:/SACR_models/SACR_FIX/yolov5x_2025_surveys_conf20_June9_gr5_cranes.csv")
#dest1 = "D:/SACR_models/SACR_FIX/survey_images_2025_subset/"

# image_dir = "D:/WHCR_2025/1_parent_images/JPG_20250122_131500/"
image_dir = "D:/WHCR_2025/12_WHCR_detection/e_tiles_5perc_empty"

csv_data = pd.read_csv("D:/WHCR_2025/12_WHCR_detection/dataset_Aug3_no_empty/train_image_list.csv")

dest1 = "D:/WHCR_2025/12_WHCR_detection/dataset_Aug3_no_empty/train/images/"

if not os.path.exists(dest1):
    os.mkdir(dest1)

##if jpg is needed run this:
csv_data['unique_image_jpg'] = csv_data['unique_image_jpg'] + ".jpg"

x = 0

csv_list = []
csv_list = csv_data['unique_image_jpg'].tolist()
print(csv_list)

for root, dirs, files in os.walk(image_dir):
    for filename in files:
        if filename in csv_list:
            x = x + 1
            print ("Copied: ", x)
            path = os.path.join(root, filename)
            print ("path " , path)
            shutil.copy(path, dest1)  # can be shutil.move or shutil.copy
        else:
            pass

