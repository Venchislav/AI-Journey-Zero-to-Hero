# Essence of Linear Algebra 2
Today I'm studying Essence of Linear Algebra 2:
Topics: #Math #Math #MathForML #3b1b #linalg
Course:  [Essence of Linear Algebra by 3b1b](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
Progress: Gain the power guys!
___
Notes:

Starting from Question:
- Does order matter in Matrix Multiplication

$$AB == BA ?$$
Of course we could start our calculations and so on, but thinking logically:
$$AB \neq BA$$
Our Matricies are transformations. (If ya don't remember check [[Essence of Linear Algebra 1]])

If we shear and then rotate 90 deg (for example) it's not same as rotate 90deg and shear
(Imagine it in your head)
Here's an explanation (I don't remember if Grant put it)
(Spoiler: I was right, I even gave same example)

<html><iframe width="560" height="315" src="https://www.youtube.com/embed/XkY2DOUCWMU?si=l3cxkJpMGuyQoZop&amp;start=455" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></html>
I also remember it from MML book (part I've read), but there it wasn't explained

BTW: I dont remember if I wrote it in previous note, but we read transformations from right to left
(like function), as our matricies are similar to function.
Ahhh... Beauty of Math🌌

So there are two things:

1. Matrix Multiplication is asociative
$$(AB)C = A(BC)$$
Proof: There's a horrible mathematical proof with a lot of calculations and there's a beautiful logical explanation.

Let's start with beauty: As we're reading our matrix multiplications from right to left it doesn't matter. Really
Ugly proof is calculation (and it's f.cking nightmare)
So it's just logical that these are equal as they're same transformation applied to space
(The order is same)
___
Determinant.

In terms of space transformations determinant describes the area change of each "rectengular"
For example:
$$\begin{bmatrix} 0.5 & 0.5 \\ -0.5 & 0.5 \end{bmatrix}$$
Determinant of this transformation:
$$det(\begin{bmatrix} 0.5 & 0.5 \\ -0.5 & 0.5 \end{bmatrix}) = 0.5$$
But determinant can be a negative number
Wataheeee
Well it's because of orientation change.

In terms of $i$ and $j$ it the moment when $j$ is to the right of $i$ meaning our orientation changed.
When our determinant is negative it means we flipped our orientation and scaled space by $|det|$
Note: when we work with 3D space determinant will be representing Volume of parallelepiped.
To check if orientation was flipped we need to use right hand rule.
![[Pasted image 20240401223328.png]]
If we can apply this rule with our right hand after transformation: congrats!
Determinant > 0.
But if we can do it only with left hand:
Determinant < 0
<html><iframe width="560" height="315" src="https://www.youtube.com/embed/Ip3X9LOh2dk?si=ltiFfNKZ-6Uw6rqc&amp;start=420" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></html>

Determinant calculation formula:

$$det(A) = a\times d - c \times b$$Where A:
$$A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$$
![[Pasted image 20240401223805.png]]
___
Done!
For today it's done!

Task for tomorrow:
![[Pasted image 20240401223932.png]]
