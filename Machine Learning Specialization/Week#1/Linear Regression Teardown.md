# Linear Regression Teardown
document written by Venchislav
___

# 0.0        INTRODUCTION

Basical Machine Learning is divided on 2 main spheres:

- Regression
- Classification


Regression - method of predicting continuous values.
Classification - method of predicting finately ranged categorical variable

Today we're speaking about Regression.
___

Examples of Regression:

- Price prediction of house by it's area
- Churn prediction for company
- Bitcoin price prediction by historical data


# 1.0       Linear Regression.

Linear Regression is the easiest and most famous machine learning algorithm.

It was firstly discovered as a statistical method, but then was tuned and enhanced as a Machine Learning Model.

This model predicts our $\hat y$ with simple linear formula you may remember from school:

$$y = wx + b$$

This formula is nothing new, but here's a quick reminder:

$w$ - slope.  Parameter descirbing how steep our line is
$b$ - y-intercept or *bias*.  It's y value at x=0.

<img src='https://images.spiceworks.com/wp-content/uploads/2022/04/07152950/26-3.png' width=30%>


We can compute our linear regression coefficients statisticaly (using 1 formula):

$$b = {sd_y \over sd_x} * r_{xy}$$
$$w = \overline Y - b \overline X$$

And it may seem a good solution, but actually it's not.

In real world our data is complex and *multidimensional* making this method inefficient.

Now we Can dive into 2 main concepts building Linear Regression:

# 2.0      Cost Function

Cost function/loss function doesn't matter how it's named.  What it does is way more important.

Here's a question:

"*How can we describe efficiency of our line with 1 numeric value?*"

I mean. Why this line:

![[Pasted image 20240428125733.png]]

Is better than this:

![[Pasted image 20240428125749.png]]

Cost function kicks in!

Idea is very simple:

- For each 'dot' we calculate distance between $\hat y$ and $y$
- We square it (explained lower)
- We divide it by number of dots

-But why df do we square it. It's abs operation in there!

Well, we could use abs, but square is just better, because:

1. It works as abs.    $x^2$ can not be negative
2. It increases big mistakes (if our mistake is > 1) and decreses small mistakes (if our mistake is < 1)
3. Parabola is smoother than abs graph

# 3.0   Gradient  Descent

Gradient descent is a method of function minimization.

In our case we'll be using it to minimize our cost.

Our w, b, and cost function dependcy can be plotted like this:

<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9xbdZFyRgCLSxBbTd2jibs8nP3USPE59vUyy3Z0baHANliiGgpALBRGPOKueRC0ukCkU&usqp=CAU' width=30%>


We can slice this graph 2 times and by looking to it we'll see parabollas!

In other words we'll calculate partial derivative and substract it from our coefficents!

Without deep dive into calculus let's have it here:

$${d\over dw} J(w, b) = {1 \over m} \sum (wx_i + b - y_i) * x_i$$
$${d\over db} J(w, b) = {1 \over m} \sum (wx_i + b - y_i)$$
By simple chain rule!

# 4.0 Important Notes:

### We need to update w and b simultaneously. 
If we don't we will be calculating one of our variables partial derivatives with already updated value of 2nd parameter.

### Learning Rate

To tune speed of our learning (how big our steps are) we use Learning Rate. It shouldn't be too small (in order to avoid slow learning), but they shouldn't be too big (in order to avoid broken learning) either.

___

This material is simplified, as I don't really like writing papers.

Here are some additional sources:

https://www.youtube.com/watch?v=7ArmBVF2dCs

https://www.youtube.com/watch?v=dLc-lfEEYss&list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI&index=9

https://www.youtube.com/watch?v=KWULpBYzIYk&list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI&index=10

https://www.youtube.com/watch?v=CFN5zHzEuGY&list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI&index=11

https://www.youtube.com/watch?v=peNRqkfukYY&list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI&index=12

https://www.youtube.com/watch?v=WtlvKq_zxPI&list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI&index=15

https://www.youtube.com/watch?v=w_2vCijLiiM&list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI&index=16

https://www.youtube.com/watch?v=PKm61nrqpCA&list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI&index=17

___

See ya!
