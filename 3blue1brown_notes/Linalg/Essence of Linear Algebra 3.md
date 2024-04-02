# Essence of Linear Algebra 3
Today I'm studying Essence of Linear Algebra 3:
Class: 
Course:  [link]()
Progress:
___
Notes:

### Systems of Equations
In school math we've dealt with systems of Linear Equations. We know how to solve them and so on, but we can represent them as matricies

$$\begin{equation}\begin{cases} a = 3 \\ b + 2a = 8\end{cases}\end{equation}$$
can be represented as matrix with vectors

$$\begin{bmatrix}1 & 0 \\ 1 & 2\end{bmatrix} \times \begin{bmatrix} a \\ b\end{bmatrix} = 
\begin{bmatrix} 3 \\ 8\end{bmatrix}$$
We already know that matrix represents some linear transformation. So it means:
We're searching for $\vec x$ that turns into $\vec v$ after transformation $A$
As our system can be represented as

$$A \vec x = \vec v$$

<iframe src='https://3b1b-posts.us-east-1.linodeobjects.com/content/lessons/2016/inverse-matrices/transformation_ax=v.mp4#t=0.001' width=100% height=100%></iframe>
### Inverse Matrix Concept:
For nearly every operation there's an opposite of this operation.
Example:
<p>Rotation 90deg right  --  Rotation 90deg left</p>
This opposite transformation is an inverse of Matrix:
$$A^{-1}$$
It means if we apply Matrix to a vector and then inverse of this matrix we get same result

$$AA^{-1}\begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix} = \begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix}$$


<iframe src='https://3b1b-posts.us-east-1.linodeobjects.com/content/lessons/2016/inverse-matrices/rotation_inverse.mp4#t=0.001' width=100% height=100%></iframe>

Rank concept:

<u>Rank of matrix</u> represents number of dimension of it's output

In different books They are written as:
$$R^n$$

<iframe width="560" height="315" src="https://www.youtube.com/embed/uQhTuRlWMxw?si=Td5J8KUjyiEppOj_&amp;start=487" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


### Null Space and Vector Space

Null Space: Kind of "set" of vectors that land on the origin of our plane. These are also called kernel vectors. After space squicsh applied they land on the origin

Column Space: Span of columns of our matrix. It represents all possible outputs of $A \times \vec v$
The thing is:
Matricies represent basis vector coordinates. In this way it also represents transformation of space.
Span of basis vectors shows us all possible vectors that can be formed from basis.
___
Sum Up: Matrix inverse exists only when our matrix determinant $\neq$ 0

End of session uno Yo