# Essence of Linear Algebra 9
Today I'm studying Essence of Linear Algebra 9:
Topics: #Math #Math #MathForML #3b1b #linalg
Course:  [Essence of Linear Algebra by 3b1b](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
Progress: Till I colapse
___
Notes:

Today we will Talk about "quick trick for computing eigenvalues".

As a reminder here's the way to calculate eigenvalues in convenient way:

![[Pasted image 20240407115627.png]]

Pretty easy, right?
But there's a faster way to calculate.

For the following calculations we need to understand few concpets:
1. trace of matrix divided by 2 is mean of a and d, and it's also mean of eigenvalues:
	$${1 \over 2} tr(\begin {bmatrix} a & b \\ c & d\end{bmatrix} = {{a + d}\over2} = {{\lambda_1 + \lambda_2}\over2} = m (mean)$$
(trace of matrix is a sum of diagonal values)
2. determinant of matrix equals product of eigenvalues:
	$$det(\begin {bmatrix} a & b \\ c & d\end{bmatrix}) = ad - bc = \lambda_1 \lambda_2 = p (product)$$
	It makes sense (just see this illustration):
		![[Pasted image 20240407120416.png]]


And Finally,
We can calculate it:

![[Pasted image 20240407120550.png]]

All the things there are kinda easy to understand (really).
___
Is it easier?
Idk😪.
___
Alright let me try to solve one!

![[Pasted image 20240407121058.png]]

1. Mean is gonna be: 5 ((8 + 2) / 2)
2. Product is gonna be: 9 ($det(\begin {bmatrix} 2 & 7 \\ 1 & 8\end {bmatrix})$)
3. Now solve it:
$$\lambda = m \pm \sqrt{m^2 - p}$$

It equals: 
$$\lambda = m \pm \sqrt{25 - 9} = m \pm \sqrt{16}$$


We get:
$$\lambda = 5 \pm 4$$
$$\lambda_1 = 9$$
$$\lambda_2 = 1$$
___
To sum up this method can be helpful, but it may seem odd to do so many things instead of simple quadratic equation solving. Well... sometimes...
The best thing about this video and this beautiful note is the understanding of connection between trace and eigenvalues and so on. (dude, I didn't even know what the trace of matrix is)

Alright, hope this note is good!
___
See ya!

<img src='https://habrastorage.org/r/w1560/webt/an/ua/vw/anuavwiv2xhtnyh2yjkcqw8gzcc.png' width=75%>

