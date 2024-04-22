library(datasets)

?mtcars

# The data was extracted from the
# 1974 Motor Trend US magazine,
# and comprises fuel consumption and
# 10 aspects of automobile design and
# performance for 32 automobiles
# (1973–74 models).

head(mtcars)

barplot(mtcars$cyl)  # sh🎸t as it builds plot of cylinders distribution
# we don't give a duck about it

# so let's create variable of special data type (table)
cylinders <- table(mtcars$cyl)  # create cylinders data object

barplot(cylinders)  # this works fine (it's kind of count plot of our cylinders)
plot(cylinders)  # same plot, but with lines instead of bars


# yeah... R is trash (remember?)
# so we assign variables here in
# UGLY way...

pisya <- 'Hello world!'
print(pisya)  # Hello world!

pisya = 'Goodbye world!'
print(pisya)  # Goodbye world!

# Thanks to God! I thought that ugly thing is the only way...


