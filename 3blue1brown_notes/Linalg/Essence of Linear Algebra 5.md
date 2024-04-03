# Essence of Linear Algebra 5
Today I'm studying Essence of Linear Algebra 5:
Topics: #Math #Math #MathForML #3b1b #linalg
Course:  [Essence of Linear Algebra by 3b1b](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
Progress:
___
Notes:

### Cross Product
Cross product is pretty tricky topic for me (as I had difficulties with understanding it on DeepLearningAI course). But it's pretty easy.

Cross product can be represented as area of pareallelogram, spaned by vector $\vec v$ and $\vec w$.
Order Matters, cross product may be negative!
<h3>Our cross-product is positive when v is on the right of w (think of unit vectors i and j)</h3>

![[Pasted image 20240403162857.png]]

Now the most important thing.

Cross Product is calculated as:
$$\vec v \times \vec w = det(\begin {bmatrix} v1 & w1 \\ v2 & w2\end{bmatrix})$$
It's pretty logical.
Our vectors can be represented as transformed unit vectors. This transformation turned
$$\begin {bmatrix} 1 & 0 \\ 0 & 1\end {bmatrix}$$
into 
$$\begin {bmatrix} v1 & w1 \\ v2 & w2\end{bmatrix}$$
And determinant describes how each quadratic changed.
If our orientation flipped our determinant is negative. 

In 3d space we can use right hand rule to find direction of vector cross product.

![[Pasted image 20240403163910.png]]

Our thumb will be pointing direction of cross product.

To calculate cross product in 3d we need to find determinant of:
$$det(\begin {bmatrix} \hat i & v1 & w1 \\ \hat j & v2 & w2\\ \hat k & v3 & w3\end{bmatrix})$$

What on earth does it mean? Grant said the proof will be in the next video for curious guys. (I'm curious)
___
Properties of 3d cross product.
1. It's vector
2. Lenght of this vector is parallelogram's are
3. It's direction can be found by right-hand rule
4. It's perpendicular to v and w

<img src='https://i.ytimg.com/vi/U7CZcd-UYmU/maxresdefault.jpg' width=33%>

There's a pretty complicated explanation so...
Less go.

We can define our cross product a volume of parallelogram, but replacing the first column with some variables (x y z for example)
We get:
![[Pasted image 20240403170924.png]]
But our function can be implemented as a liner tranformation.
We can replace it with matrix multiplication in other words:

![[Pasted image 20240403171025.png]]

Let's call this mystery 3d vector p, and let's calculate some things:
![[Pasted image 20240403171107.png]]

We get that each element of p equal some value calculated through determinant.
![[Pasted image 20240403171202.png]]

In geometrical interpretation:
Perpendicular xyz vector projection multiplied by parallelogram area.
But that's identical to taking a dot product of vector, that's perpendicular to area of v and w and vector that has a lenght of parallelogram area.
In this way we found our p vector.

Here's my guess why we multiply it by xyz projection (not by xyz vector):

As far as I understand, we take the projection of the xyz vector at 10:26, since we are calculating the volume of the parallelepiped, which is calculated as the product of the area of the base of the parallelepiped and the height of the parallelepiped (S*h). We calculate the area of the base (the 2d cross product of the vectors v and w) and multiply it by the xyz projection (since we need the height to calculate the volume). As Grant said, this is identical to: the projection vector xyz times the vector with the length of the base area (we're using the dot product here since we're working with 3D vectors). This way we calculate p.

It's my youtube comment, that's why it's so official.
That's pretty much it!
See ya!
(I spent additional hour on understanding, jeez)
___
2 Sessions Passed💪