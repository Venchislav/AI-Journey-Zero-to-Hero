# Today we're working with plots in R

library(datasets)

# Load Iris dataset - famous dataset
head(iris)

?plot

# plot function is optimized for different data types

# for categorical data:

plot(iris$Species)  # bar chart
plot(iris$Sepal.Length)  # scatter of index and length
plot(iris$Species, iris$Petal.Length)  # box plots
plot(iris$Petal.Length, iris$Petal.Width)  # scatter

plot(iris)


plot(dnorm, -3, 3)  # normal distribution from -3 to 3 with std=1
plot(exp, 0, 10)

# and of course we can customize our plots:

plot(
  dnorm,
  -3,
  3,
  lwd=5,
  col='#1DB954',
  xlab='z-score',
  ylab='density',
  main='Standard Normal Distribution with Spotify Color'
)
