import sahi.predict
import os
import csv
import torch
import sahi
import pandas as pd
import yolov5

# YOLOv5 training is done on the command line!
# For inference that outputs a csv file with detections:
# Inputs: root_dir = folder with images;
#         new_csv = detection csv to output
#         model_path = path to YOLOv5 weights file

# root_dir = "D:/SACR_models/SACR_FIX/2023_images_gr5_cranes_yolov5/"

# usea SACR2025 conda eviron
root_dir = "D:/SACR/8_FINAL_2025_results/test_data_not_complete/"
new_csv = "D:/SACR/8_FINAL_2025_results/more_test_data_temp3.csv"

#2025:
#model_path = "C:/users/aware/desktop/MODELS FOR USE/sacr_2025_yolo_v5.pt"

#2023:
model_path = "D:/SACR/model_weights/yolov5x_update_for_2025/weights/best.pt"

#model_path= "C:/Users/aware/Desktop/MODELS FOR USE/ducks_as_background.pt"
# visual_path = "D:/SACR/SACR_FIX/visuals_2025/"

visual_path = "D:/SACR/8_FINAL_2025_results/new_tiles_viz_test_temp/"

device = "cuda:2" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")
use_cuda = torch.cuda.is_available()

if device:
    print(torch.cuda.get_device_name())

if not os.path.exists(visual_path):
    os.mkdir(visual_path)

detection_model = sahi.AutoDetectionModel.from_pretrained(
    model_type = 'yolov5',
    model_path = model_path,
    confidence_threshold=0.20,
    device="cuda:2",  # or 'cuda:0'
)

with open(new_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['unique_image_jpg', "bbox", "class", "score"])

for root, dirs, files in os.walk(root_dir):
    for file in files:
        source = os.path.join(root, file)
        print(source)
        result = sahi.predict.get_sliced_prediction(
            source,
            detection_model,
            slice_height=400,
            slice_width=400,
            overlap_height_ratio=0.2,
            overlap_width_ratio=0.2,
            postprocess_class_agnostic = True,
            postprocess_match_metric= 'IOU',
            postprocess_type= 'GREEDYNMM',
            postprocess_match_threshold= 0.1 #0.20
        )
        object_prediction_list = result.object_prediction_list
        base = os.path.basename(file)
        result.export_visuals(file_name=base, export_dir= visual_path, hide_labels=True,
          hide_conf=True, rect_th=1)

        with open(new_csv, 'a', newline='') as file:
            writer = csv.writer(file)
            for result1 in object_prediction_list:
                writer.writerow([source, result1.bbox, result1.category, result1.score])

csv_data = pd.read_csv(new_csv)

filename = csv_data['unique_image_jpg']

bbox = csv_data['bbox']
csv_data['score'] = csv_data['score'].str.replace(r"PredictionScore: <value: ", '', regex=True)
csv_data['score'] = csv_data['score'].str.replace(r">", '', regex=True)
csv_data['class'] = "sandhill_crane"

csv_data['bbox'] = csv_data['bbox'].str.replace(r"BoundingBox: <", '', regex=True)
csv_data['bbox'] = csv_data['bbox'].str.replace(r">", '', regex=True)
csv_data[['xmin', 'ymin', 'xmax', 'ymax', 'w', 'h']] = csv_data['bbox'].str.split(',', expand=True)
csv_data['h'] = csv_data['h'].str.replace(r"h: ", '', regex=True)
csv_data['w'] = csv_data['w'].str.replace(r"w: ", '', regex=True)
csv_data['xmin'] = csv_data['xmin'].str.replace(r"(", '', regex=False)
del csv_data['bbox']

csv_data.to_csv(new_csv)
