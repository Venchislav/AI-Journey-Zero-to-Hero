# Essence of Linear Algebra 7
Today I'm studying Essence of Linear Algebra 7:
Today I'm studying Essence of Linear Algebra 6:
Topics: #Math #Math #MathForML #3b1b #linalg
Course:  [Essence of Linear Algebra by 3b1b](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
Progress: Unstoppable
___
Notes:

##### Change Of Basis Vector is today's topic.

At first I just thought: "why do we need to change basis vector? Like what's the point here?"
As I found out [here](https://www.quora.com/What-is-the-point-of-changing-basis-in-linear-algebra) it can reduce computations. I'm not sure, but okay...

What does it mean?

The thing is that all the time I was working with basis vectors $\hat i$ and $\hat j$
Imagine having friend from another planet (Pedro for example).

My friend Pedro has his own basis vectors with coordinates:
$$\begin{bmatrix} -2 & 1 \\ 3 & 5\end {bmatrix}$$
Pedro is a big fan of Linear Algebra. We both wath videos about it (he's a big fan of 3brown 1 blue), but there's a problem. Sometimes I don't really understand him (as he has different basis vectors).

So we can describe the same vector as different (through basis vectors)


![[Pasted image 20240405184947.png]]

So how do we _translate_ his language to our.

Here We need to refresh matricies and transformations in our mind!

We can think of Pedro's basis vectors as our transformed basis vectors.
And we can represent this transformation through matrix.
(This matrix will be representing point where our transformed basis vectors (his basis vectors) land)

$$\begin{bmatrix} -2 & 1 \\ 3 & 5\end {bmatrix}$$
And some vector translation from his language to our will look as:

$$\begin{bmatrix} a1 \\ b1 \end {bmatrix} = \begin{bmatrix} -2 & 1 \\ 3 & 5\end {bmatrix}\begin{bmatrix} a \\ b\end{bmatrix}$$

Where a1 b1 - our vector and b - pedro's vector.

It's pretty easy idea to understand.
And it's easily come up to our mind that translation from our language to his is simply inverse of this transformation matrix:
$$\begin{bmatrix} -2 & 1 \\ 3 & 5\end {bmatrix} ^ {-1}$$
EZY yo!

But how do we apply some transformations on his basis vectors?
For example we have some transformation (90$\degree$ left rotation)
How do we rotate his vector?

$$\begin{bmatrix} 0 & -1 \\ 1 & 0\end {bmatrix}$$

Well it may seem that we can simply translate this rotation matrix from _our language_ to _his language_
<h3>"But that's not quiet right" - Grant Sanderson</h3>
Instead we need to refresh idea of transformations applience (when we apply few transformations on matrix)

We need to:
1. Translate his vectors to our language
2. Apply this transformation to translated vector
3. Translate it back to Pedro's Language
So we get some kind of a train (that we read from right to left)

It may something like this:

$$\begin{bmatrix} -2 & 1 \\ 3 & 5\end {bmatrix}^{-1}\begin{bmatrix} 0 & -1 \\ 1 & 0\end {bmatrix}\begin{bmatrix} -2 & 1 \\ 3 & 5\end{bmatrix}\begin{bmatrix} -1 \\ 2\end{bmatrix}$$
Read it from right to left:
We have Pedro's vector
We translate it to our language
We apply rotation to it
We translate it back to Pedro's language.

This is incredibly beautiful topic, as linear algebra imho shows it's best here (in visualization part)
___
Cool!
End of session number 1!

<img src='https://cdn.akamai.steamstatic.com/steam/apps/557340/capsule_616x353.jpg?t=1686262019'>
