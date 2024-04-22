# Today we are gonna be building histograms
# Easy sh.t

# btw I know it's f🍤cking useless
# I know that ML engineers use python

# I love python, but I just want to try some new stuff

library(datasets)

head(iris)

# simple histograms:
hist(iris$Sepal.Length)
hist(iris$Sepal.Width)
hist(iris$Petal.Length)
hist(iris$Petal.Width)

# parametrized histograms:

hist(iris$Petal.Width [iris$Species == 'virginica'],
     xlim = c(0, 3),  # limit of x
     breaks = 9,  # width of columns
     main = 'Virginica petal width',  # title (why df it's called main)
     xlab = 'width',  # x label
     col = 'blue'  #histogram columns color
     )


# we can also build some kind of "subplots" plot:


print(table(iris$Species))


hist(iris$Petal.Width [iris$Species == 'setosa'],
     xlim = c(0, 3),  # limit of x
     breaks = 9,  # width of columns
     main = 'Setosa petal width',  # title (why df it's called main)
     xlab = 'width',  # x label
     col = 'green'  #histogram columns color
)


hist(iris$Petal.Width [iris$Species == 'versicolor'],
     xlim = c(0, 3),  # limit of x
     breaks = 9,  # width of columns
     main = 'Versicolor petal width',  # title (why df it's called main)
     xlab = 'width',  # x label
     col = 'blue'  #histogram columns color
)


hist(iris$Petal.Width [iris$Species == 'virginica'],
     xlim = c(0, 3),  # limit of x
     breaks = 9,  # width of columns
     main = 'Virginica petal width',  # title (why df it's called main)
     xlab = 'width',  # x label
     col = 'red'  #histogram columns color
)

