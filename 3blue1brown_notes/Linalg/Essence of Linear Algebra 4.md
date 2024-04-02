# Essence of Linear Algebra 4
Today I'm studying Essence of Linear Algebra 4:
Class: 
Course:  [link]()
Progress:
___
Notes:

## Dot Product

There are 2 ways to introduce dot product:
1. Through vector calculation
2. Through geometrical essence

Vector Calculation is:

$$\begin {bmatrix} a\\ b \end {bmatrix} \times \begin {bmatrix} c\\ d \end {bmatrix} = ac + bd$$
We simply pair values of vector 1 and vector 2, multiply them, and get the result as a sum of these multiplied pairs.

When I heard it, I thought about zip() function in python and implemented it from scratch:
```python
def dot(v1, v2):
	total = 0
	for e, e1 in zip(v1, v2):
		total += (e * e1)
	return total
```
Easy hah

Geometrical Essence:

Dot product is a product of length of vectror1 and length of vector2 projection (such that vector1 and vector2 are on the same line (in 2d case)).
Here's illustration on it:

<img src='https://www.3blue1brown.com/content/lessons/2016/dot-products/figures/geometric-interpretation/GeometricInterpretation.svg'>

But here, if our w vector projection has opposite direction dot product will be
negative.

Order doesn't matter, as we're working with numbers.
___

<img src='https://i.imgflip.com/8bsifr.jpg' width=30%>

Proof of projection to dot product is tricky.
Well...
We take coordinate plane
On this plane we have some diagonal line.
It situated like this that we have vector $\vec u$ in space, such that line goes through his origin and tip.

<img src='https://www.3blue1brown.com/content/lessons/2016/dot-products/figures/unit-vector/NumberLineFormedByUnitVector.svg'>

Now, setting projection of random vectors on this line is linear transformation, as evenly spaced dots save their pattern. 
So, projection represents some linear transformation, and to describe linear transformation as matrix we need to find coordinates where $\hat i$ and $\hat j$ land.
So, let's go

<img src='https://www.3blue1brown.com/content/lessons/2016/dot-products/figures/unit-vector/NumberLineFormedByUnitVectorIHatJHat.svg'>

After putting a symmetry line:

<img src='https://www.3blue1brown.com/content/lessons/2016/dot-products/figures/unit-vector/NumberLineFormedByUnitVectorIHatSymmetryUHat.svg' width=33%>

We understand that projection of i on u equal to projection of u on i, so we can write it to our matrix.
The same thing is about y axis.
After this we have:
$$\begin {bmatrix} u_{x} & u_{y}\end {bmatrix}$$
It's matrix representing our transformation. So applience of this matrix looks like:

$$\begin {bmatrix} u_{x} & u_{y}\end {bmatrix} \times \begin {bmatrix} a \\ b\end {bmatrix}$$
But as our matrix is 2x1 we understand that it's absolutely the same to dot product:

$$\begin {bmatrix} u_{x} & u_{y}\end {bmatrix} \times \begin {bmatrix} a \\ b\end {bmatrix} = u_{x}a + u_{y}b$$
Identical to:
$$\begin {bmatrix} u_{x} \\ u_{y}\end {bmatrix} \times \begin {bmatrix} a \\ b\end {bmatrix} = u_{x}a + u_{y}b$$
which is a dot product.
BANG!!!
(You know, after this explanation I understood it💀)

But here we explained it in context of unit vectors (I call them base vectors - cuz it's similar to russian version (базовый вектор)).
Anyways, any vector on this diagonal 1D line will be scaled version of unit vector $\vec u$
So it appears any projection will be scaled (that's why we multiply lengths)

To finish it:

This was a great example of _duality_.
As Grant said, it's some natural, but surprising correspondence.
And yeah, that's true! That was great, absolutely!

___
Note for myself:
1. It's really important to make such notes (as I understand topic deeper)
2. Obsidian has a pretty cool note editor😎

See ya!
<img src='https://media1.tenor.com/m/M-gzqVC_7NAAAAAd/dj-khaled.gif'>