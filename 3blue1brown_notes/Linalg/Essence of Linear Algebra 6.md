# Essence of Linear Algebra 6
Today I'm studying Essence of Linear Algebra 6:
Topics: #Math #Math #MathForML #3b1b #linalg
Course:  [Essence of Linear Algebra by 3b1b](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
Progress: Let's goooooo🤡
___
Notes:
### Cramer's Rule

Cramer's rule is a way of linear equations solving
Steps we take to proof it:
1. Write system of equations as a transformed unknown vector.
![[Pasted image 20240404171804.png]]

3. Apply transformation on space.
![[Pasted image 20240404171838.png]]

5. Calculate area of Parallelogram (in 2d) that is enclosed by one of the transformed basis vectors and our unknow scaled vector (we know it as answer)

![[Pasted image 20240404171907.png]]

7. You'll get that it equals one of the unknown's vector coordinates (x or y in 2d)
8. You get that transformed area will be one unknown's vector coordinates (we got it in step 2) and it will be scaled by our transform matrix determinant (how our area is changed)
9. We get:
$$Area=det(A)y$$
(for example when we enclosed parallelogram by i and unknown vector)
from here we can solve y
$$y = {Area \over det(A)}$$
And our area is a determinant of matrix with one of the original coordinates and one unknow vector replacing basis
![[Pasted image 20240404171733.png]]
___
So it's more like a legacy stuff, but still pretty important for concepts understanding!
<iframe width="560" height="315" src="https://www.youtube.com/embed/jBsC34PxzoM?si=Rw51GN0EmBAC7QC8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

C ya!