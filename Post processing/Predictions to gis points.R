
library (raster)
library (rgdal)

setwd(file.path('D:', 'SACR', '4_FINAL_2023_results'))


## Inputs
data1 <- read.table ("mosaics17a_c_2023_step2.csv",sep = ",", 
                     header=TRUE, fill=TRUE)
gsd_m = 0.103 
output_predictions <- "predict_sacr_2023_17a_c.csv"

data1$xmin_m <- data1$xmin*gsd_m
data1$ymin_m <- data1$ymin*gsd_m

data1$h_m <- (data1$h*gsd_m)/2
data1$w_m <- (data1$w*gsd_m)/2

data1[0:5,]

data1$ymax_exten <- NULL
data1$xmax_exten <- NULL
data1$y_annot_ab <- NULL


data1$x_annot <- data1$xmin_extent + ((data1$xmin_m)+ data1$w_m)
data1$y_annot <- data1$ymax_extent - ((data1$ymin_m)+ data1$h_m)
data1$y_annot_above <- data1$y_annot + 0.10

data1$x_annot <- as.numeric(data1$x_annot)
data1$y_annot <- as.numeric(data1$y_annot)
data1$y_annot_above <- as.numeric(data1$y_annot_above)

names(data1)

write.table(data1, output_predictions, sep=",", row.names=FALSE)
