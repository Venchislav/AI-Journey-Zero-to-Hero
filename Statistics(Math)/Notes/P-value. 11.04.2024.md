# P-value. 11.04.2024
Today I'm studying P-value. 11.04.2024:
Class: Intro To Statistics (Russian language)
Course:  [link](https://stepik.org/course/76)
Progress: That's alright like
___
Notes:

Now we know how to calculate mean of our population and confidence interval.
But really important part of statistics is a hypothesis proof.

For example we are testing new drug on 64 patients. Mean of population is 20 ($\mu = 20$) while our sample's mean is 18.5 ($\overline x = 18.5$).
Can we say that it's affect of new drug, or it's just luck?

Here it goes!

We have 2 possible results here:

H0:
$$\mu_{nd} = 20$$
(Our new drug has no effect. It's just because of sample)

H1:
$$\mu_{nd} \ne 20$$
(Our drug has effect on our patients)
___

To proof it we can assume that H0 is right (Drug doesn't matter anything)

Then we can build our means distribution
(via Central Limit Theorem)

After calculating se:

For these values: 
$$N = 64; \overline X = 18.5; sd=4$$
We have  $se = 0.5$

Know let's calculate difference between our population mean (In case of H0 our distribution's mean will be $\mu$) and sample mean.

$$z = {x_i - \overline x \over sd}$$

Since now we can calculate probability of it (in our case z-score is -3)

Assuming both tails (-3 and 3) our p value is 0.0027.
If our p value is less than 0.05 we can throw H0 away. If not we can't throw H0 away, but we can't say that H1 is impossible. There's nothing we can do...

$$P < 0.05$$
___
I also will try to write notes on T-distribution. (I have it my paper notebook, but I also want a digital version)

C ya!
___
