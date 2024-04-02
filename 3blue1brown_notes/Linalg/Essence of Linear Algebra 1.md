# Essence of Linear Algebra 1
Today I'm studying Essence of Linear Algebra 1:
Topics: #Math #Math #MathForML #3b1b #linalg
Course:  [Essence of Linear Algebra by 3b1b](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
Progress: Good. I'm trying to be better
___
Notes:
- _Vector_. There are many use cases of vectors, but in linear algebra these are some kind of array-like mathematical type. In Geometry it represents dot location:

$$\vec{a} = [1, 2]$$
It's a vector above saying us that in 2D space our dot is located on 1x and 2y

I skipped 2 vids

<u>_linear transformation_</u> - sort of transformation where origin doesn't change and girdlines are parallel. (meaning our line isn't deformed)
Our transformation may be written as:

$$\vec{a} = c \times transf(i) + d \times transf(j)$$

![[Pasted image 20240401164324.png]]

We can write it in better way:

$$[x y] = x[1, -2] + y[3, 0] =
\begin{bmatrix} 1x + 3y \\ -2x + 0y \end{bmatrix}
$$
where i = [1 -2] and j = [3 0]

Excercise:
- Calculate position of vector that is 5i + 3j (following new coords)
- Calculate position of vector 15i + 8j (following new coords)

Matricies - special math data type with rectengular shape containing values in rows and columns.

We can represent our basis vector positions as matrix:

![[Pasted image 20240401165322.png]]

We can describe our linear transformations as matix by vector multiplication following our formula above

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix} \times \begin{bmatrix} x \\ y \end{bmatrix} = x \begin{bmatrix} a \\ c \end{bmatrix} + y \begin{bmatrix} b \\ d \end{bmatrix} = \begin{bmatrix} ax + by \\ cx + dy\end{bmatrix}$$
Excercises:
- Write 90 degree rotation transformation as matrix
- Calculate position of vector [2, 3]

Summing up speech about matricies:
think of them as some space transformations.
<img src='https://i.makeagif.com/media/9-22-2016/oWJ8og.gif'>
Speaking with programmin lang matricies are kinda functions.
Let's implement one for fun:

```python
def matrix_transformation(vector, matrix):
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]
	return [a * vector[0] + b * vector[1], c * vector[0] + d * vector[1]]
```
___

# Matrix Multiplication

sometimes In linear algebra we want to apply 2 or more transformations of the space.
Like rotate our space 90 degree and then apply some _shear_

It's called <u>composition</u>.
![[Pasted image 20240401171856.png]]

Our transformations are read from right to left:

![[Pasted image 20240401172349.png]]

We multiple column of matrix M1 by matrix M2 and then do same like this with 2nd column of M1
___
End of Note for 1st study session💪