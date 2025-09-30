import pandas as pd
import numpy as np
import glob
import os
from skimage import io

# Input: files = directory of files, export_csv = csv that reports brightness
files = glob.glob("E:/2025_SACR_imagery_data/2_imagery_in_survey/*.tif")

export_csv = "E:/2025_SACR_imagery_data/brightness_2025.csv"

mean_list = []
image_list = []
for file in files:
    print(file)
    file1 = os.path.basename(file)
    img = io.imread(file)
    mean_list.append(np.max(img))  ## max for land/water
    image_list.append(file1)

pd.DataFrame({"unique_image": image_list, "max": mean_list}).to_csv(export_csv, index=True)