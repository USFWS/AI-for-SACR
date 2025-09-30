
## When converting from csv to COCO annotation format, both a unique image 
## number and a unique annotation number are needed; this scripts creates
# those fields

library(dplyr)

setwd(file.path('D:', 'SACR', '8_FINAL_2025_results'))

data1 <- read.table ("more_test_data.csv", sep =",", header=TRUE, fill=TRUE)

#data1$id <- 0
data1$image_id <- data1$unique_image_jpg
# unique id per parent image
data1$image_id <- as.numeric(factor(data1$image_id))

data1$image_id  
# unique id per annotation
#data1$id <- data1 %>% group_indices (unique_BB)

View(data1)

write.table(data1,"more_test_data2.csv", col.names=TRUE, row.names=FALSE, sep=",")
