library(dplyr)
library(ggplot2)

raw <- read.csv('height.csv',header=TRUE)
data <- tibble(raw)
m = 0.0056
g = 9.81

data <- mutate(data,
     gpe=m*g*height_m,
     lost=0.255-gpe)

print(summarise(data,
	mean_h=mean(height_m),
	sd_h=sd(height_m),
	mean_gpe=mean(gpe),
	sd_gpe=sd(gpe),
	mean_lost=mean(lost),
	sd_lost=sd(lost)))
	