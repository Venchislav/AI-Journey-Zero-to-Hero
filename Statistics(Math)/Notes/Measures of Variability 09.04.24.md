# Measures of Variability
Today I'm studying Measures of Variability:
Class: Intro To Statistics (Russian language)
Course:  [link](https://stepik.org/course/76)
Progress: I'm interested
___
Notes:

Let's jump into it!
We can describe our data variability (not only some tendencies)

There are few ways to describe our data:
1. Range:
Really simple measure. We substract max value from min value:

$$R = X_{max} - X_{min}$$
```python
range = max(array) - min(array)
```

It's not really good measure as it is really sensitive to some outliers.

2. Variance (Дисперсия):

What if we calculate mean of deviations for each element in our set of values?
Well, it may sound like a good idea, but previously in [[Measures of Central Tendency]] we discussed mean properties. 3rd property looks like:

$$\sum (x_i - \mu_x) = 0$$

So trying to calculate our variance as:

$${\sum (x_i - \mu_x)}\over n$$
Is not working, as it means:
$${0 \over n} = 0$$
But we can use _square_.
So now our formula will be:

$${\sum (x_i - \mu_x)^2}\over n$$
<h3>This is our Variance</h3>

$$D = {{\sum (x_i - \mu_x)^2}\over n}$$

But our variance is larger than needed.
So we can calculate antother measure:

$$\sigma = \sqrt{D}$$

<u>BUT HERE IT'S REALLY TRICKY STUFF</u>

We need to specify where we calculate these measures.

For example:

If we're working with _sampling_ we will be using term <h3>"standard deviation" (sd)</h3> instead of sigma letter

As we use sigma when we work with population!

___

We have separation here:

1. Population:
$$D = {{\sum (x_i - \mu_x)^2}\over n}$$

$$\sigma = \sqrt{D}$$

2. Sample:

$$D = {{\sum (x_i - \overline x)^2}\over n-1}$$
$$sd = \sqrt{D}$$
___
But why do we calculate Variance for Sample with n-1?
IDK. Literally... Author of course said it's connected with degrees of freedom and we will discuss it later, but the thing is:
It gives us better results.

Here's a nice screenshot:

![[Pasted image 20240409104958.png]]

Oh...
And I see that in internet people use Capital Letter S to describe variance.

![S^2 = \frac{\sum (x_i - \bar{x})^2}{n - 1}](https://www.gstatic.com/education/formulas2/553212783/en/sample_variance.svg)

___

There are Some interesting properties of our Variance and Standard Deviation
They are pretty similar to the properties of Mean we discussed here: [[Measures of Central Tendency]]

1. $$D_{x+c} = D_x$$
$$sd_{x+c} = sd_x$$

It's fine, and I hope it's understandable. If we add some constant to _each_ value of our set we will "move" our distribution to the left or to the right.
So our distribution form will not change.

![[Pasted image 20240409110324.png]]

There are more interesting things in 2nd property:

2. $$D_{x*c} = D_x * c^2$$
$$sd_{x*c} = sd_x * c$$
But why? But How?
Imagine it in your head:

Our distribution form will be changed. (It will be wider if our c > 1 and thiner if c < 1)

![[Pasted image 20240409110542.png]]

For example our Range will be 20 - (-20) instead of 10 - (-10) that we have before multiplication.
It's true. I checked it...

![[1cdbbdde148548eb8ef337869e71e2af.png]]
