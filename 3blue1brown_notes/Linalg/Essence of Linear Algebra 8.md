# Essence of Linear Algebra 8
Today I'm studying Essence of Linear Algebra 8:
Topics: #Math #Math #MathForML #3b1b #linalg
Course:  [Essence of Linear Algebra by 3b1b](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
Progress: Cool
___
Notes:

EigenVectors And Eigenvalues.

When we apply some transformation to our space there are some vectors that are being scaled.

We can use it to describe our transformation without basis vectors and stuff.
We will get:

$$A\vec v = \lambda \vec v$$
Where $A$ - our transformation, $\lambda$ - some scalar (eigenvalue) and $\vec v$ - our eigenvector.
Scaling our eigenvector by $\lambda$ is similar to:
$$\begin{bmatrix} \lambda & 0 & 0 \\ 0 & \lambda & 0 \\ 0 & 0 & \lambda\end{bmatrix}\vec v$$
Scaling every basis vector by $\lambda$
We can also call it as:
$$(\lambda I)\vec v$$
Where I - identity matrix with 1s diagonal.
We get:

$$A\vec v - (\lambda I)\vec v = \vec 0$$
We can get:
$$(A - \lambda I)\vec v = \vec 0$$
by taking v out of the brackets.
Suppose our eigenvector is not 0.

We will get it only with $det(A - \lambda I)$ = $0$

(And it actually means that our space is being squished or stretched)
So here we need to find our $\lambda$ such that $det(A - \lambda I)$ = $0$

![[Pasted image 20240406155134.png]]

So these are operation we applied and things we came up to.

So we calculate our determinant and get something like this:

$$(3 - \lambda)(2 - \lambda) = 0$$
It means our $\lambda$ will be 3 or 2.

Seek of eigenvector is simple.

We plug eigenvalue to our matrix and solve equation:

$$\begin{bmatrix} 3-2 & 1 \\ 0 & 2 - 2\end{bmatrix} \begin{bmatrix} x \\ y \end {bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
___
There are also some transformation where eigenvalue will be the same for each eigen vector and each vector will be eigenvector.

$$\begin{bmatrix} 2 & 0 \\ 0 & 2\end{bmatrix}$$
___
Done for today!