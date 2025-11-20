
library (Metrics)
library (dplyr)

# Enter your directory
setwd(file.path('C:', 'Brad', 'fws', 'SACR_progress'))

data1 <- read.table("results_final_valid_2023_count_only.csv", sep=",", header=TRUE)
names(data1)

## Sandhill crane- 2025

data2 <- read.table("resuts_final_valid_2025.csv", sep=",", header=TRUE)
names(data2)

data2 <- sample_n(data2, 10)

# Mae
mae (data2$gt_sacr, data2$predict_sacr)

# mape
mape (data2$gt_sacr, data2$predict_sacr)

# rmse
rmse (data2$gt_sacr, data2$predict_sacr)

# mse
mse (data2$gt_sacr, data2$predict_sacr)


