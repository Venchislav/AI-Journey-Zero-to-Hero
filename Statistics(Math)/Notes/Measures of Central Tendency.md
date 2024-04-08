# Measures of Central Tendency
Today I'm studying Measures of Central Tendency:
Class: Intro To Statistics (Russian language)
Course:  [link](https://stepik.org/course/76)
Progress: Casin <img src='https://media1.tenor.com/m/LYUe1FNHN-UAAAAC/cat-headphones.gif' width=3%>

___
Notes:

Okey Dokey...
Our data has some _Distribution_

But how can we describe this distribution with one number.
There are few ways to do it.

1. Mode(Мода) - value of measured feature, that appears most frequently.
To display it we can build "dot plot".
We can have one mode, or 2 or 3 or more.
(But keep in your head that mode is the most frequent feature value, so number of modes can not be equal to number of feature values)

2. Median - value of feature, that divides _sorted_ set of data to _halfs_
To explain easier for fellow coders:
```python
def get_median(arr):
  if len(arr) % 2 == 1:
    return arr[(len(arr) // 2)]
    
  else:
    return (arr[(len(arr) // 2)] + arr[(len(arr) // 2) -1]) / 2
```

3. Mean - sum of all values of feature divided by number of values:

It's easy brah! You learned it in secondary school.
But there's interesting moment:
We use $\overline x$ to write mean of our sample and $\mu$ to write mean of our population.


Why don't we always use mean?
Well, cuz it's too bad for some <u>outliers</u>

For example when we measure height we can have Colossal Titan with 60 meter height. Our mean will be f👏cked up with this value.

<img src='https://static.wikia.nocookie.net/shingekinokyojin/images/7/78/Armin_Arlelt_%28Anime%29_character_image_%28Colossal_Titan%29.png/revision/latest?cb=20220222211301' width=30%>

___

When our distribution is unimodal (it has only 1 mode) and symmetric. 
Good example here is gaussian distribution:

<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT79GWECr1uMcryFunlFU67yWfywbLJ_QMQY2FpO2QSGA&s'>

We can use any of these measure, but when we have outliers or our distribution is assymetrical it's better to use median or mode (depends on situation)
___
Properties of Mean:
<h1>1.</h1>

$$\mu_{x + c} = \mu_x +c$$
If we add some value (c) to every element of our set mean will change on this very value c.

We can think of it as a movement of our distribution:

![[Pasted image 20240408192158.png]]


<h1>2.</h1>

$$\mu_{x*c} = \mu_x * c$$
If we multiply every element of our set by some value (c) our mean will be also multiplied by this very value c.

<h1>3.</h1>

$$\sum (x_i - \mu_x) = 0$$

This one is more tricky...
If we subtract mean from every distribution value and get sum of those operations this sum will be 0 (I think I expressed idea in really poor way sorry for my English)

It's good to think of normal distribution.
Our values will be in kind of ballance (values will cancel out each other)

Hope it's understandable...
___
<img src='https://media1.tenor.com/m/p53Nyf0vv8sAAAAd/homelander-cinema-homelander.gif'>
