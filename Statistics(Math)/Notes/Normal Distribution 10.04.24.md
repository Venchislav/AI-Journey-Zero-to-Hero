# Normal Distribution 10.04.24
Today I'm studying Normal Distribution 10.04.24:
Class: Intro To Statistics (Russian language)
Course:  [link](https://stepik.org/course/76)
Progress: Powercore
___
Notes:

It's the best distribution to work with in statistics as it is:
- Unimodal
- Symmetrical
- Deviation of values obey probability rule.

A lot of real-life data are normaly distributed.

<img src='https://www.scribbr.com/wp-content/uploads/2023/02/standard-normal-distribution-example.webp'>

___

## Standartization

It's also called as z-transformation.

Key thing here is to transform our distribution Z-scores (special scale) such that:
$$\mu_z = 0$$
$$D_z = 1$$

To do it we use formula:
$$Z_i = {x_i - \overline x \over sd_x}$$

If we substract some const c from our mean mean will change on the same number c. In our case $\overline x$ is c.

$$\overline x - c = \overline x - \overline x = 0$$

In such way we change our mean to 0.
Now let's set Variance D to 1:

$$D_x * ({1\over sd_x})^2$$

But it is:

$$D_x * {1\over D_x} = 1$$
Ta dam!

___
Btw. I said that our distribution obeys probability rule.
It means that:

68% of our values are located at $\mu_x \pm \sigma$
95% of our values are located at $\mu_x \pm 2\sigma$
100% of our values are located at  $\mu_x \pm 3\sigma$

There's a great website for percentage calculations.
(Like how many people have IQ > 150? etc.)

https://gallery.shinyapps.io/dist_calc/
