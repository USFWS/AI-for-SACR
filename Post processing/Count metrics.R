
library (Metrics)

# Enter your directory
setwd(file.path('C:', 'Brad', 'fws', 'SACR_progress'))

data1 <- read.table("results_final_valid_2023_count_only.csv", sep=",", header=TRUE)
names(data1)

## Sandhill crane- 2025

data2 <- read.table("resuts_final_valid_2025.csv", sep=",", header=TRUE)
names(data2)

# Mae
mae (data1$gt_sacr, data1$predict_sacr)

# rmse
rmse (data1$gt_sacr, data1$predict_sacr)

# mse
mse (data1$gt_sacr, data1$predict_sacr)

# mape
mape (data1$gt_sacr, data1$predict_sacr)
