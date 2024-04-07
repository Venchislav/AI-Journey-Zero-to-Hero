# Essence of Calculus 1
Today I'm studying Essence of Calculus 1:
Topics: #Math #Math #MathForML #3b1b #calculus
Course:  [Essence of Linear Algebra by 3b1b](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
Progress: Life's Good (not LG commercial)
___
Notes:

Well, I've watched 1st episode of calculus essence, and...
It will be hard to rewrite key concepts here.

Let's start from random thing:
Circle

How do we calculate area of Circle?
Well from school you may remember formula:
$$S= \pi r^2$$
But how can we get it? Mathematicians came to it, but how?
___
We can slice our circle on many many really _thin_ rings:

![[Pasted image 20240407155308.png]]

Now taking any of these rings and unfold (I'm not sure if this word is suitable here, as I'm not native english speaker) will give us some kind of "tape".
Assuming these rings are sooo thin we can calculate area of this tape as a rectangular:

![[Pasted image 20240407155614.png]]

Area will be:
$$dr * 2\pi r$$
$2 \pi r$ - perimeter of circle (Mathematicians already knew this formula from pi defenition)

No we can allocate all those slices on coordinate line:

<iframe src='https://3b1b-posts.us-east-1.linodeobjects.com/content/lessons/2017/essence-of-calculus/figure-4.18-5.08-trimmed.mp4#t=0.001'></iframe>

Now area calculation may look like a terrifically big sum, but with really high approximation (very very very very thin lines) we will get something like this:
![[Pasted image 20240407160008.png]]
But it's area of triangle!
Furthermore, our triangle is a right triangle, so formula will be:
$$S = {1 \over 2}ab$$
In our case it will be:
$$S = {1 \over 2}2\pi r *r$$
It transforms into:
$$S = \pi r^2$$
BAM!!!!!!

But guys, wtf?
How did you accept this "approximation"?
Math is precise, or is it?

<img src='https://media1.tenor.com/m/VWevehP7cCAAAAAC/monkagigaftmichaelfromvsauce-monkagiga.gif' width=25%>

___
The actual thing that it's precise and logical.
Technicaly It's not forbidden to pick INSANELY thin slices (that we can not even imagine).
Then this precision will work.

Now...

Why do we care about circle area?

Well... Let's pick some function, for example:
$$f(x) = x^2$$
Graph of such function is a parabola.
Now how do we find area under this graph?
(btw. area under graph is called an integral)

Again, we can slice it all on veeeeeery small rectangles:

<iframe src='https://3b1b-posts.us-east-1.linodeobjects.com/content/lessons/2017/essence-of-calculus/figure-11.49-12.19.mp4#t=0.001'></iframe>

Our area of such rectangle ($dA$) will be approximately equal to $x^2$ (y side of rectangle) and $dx$ (some really tiny number we picked for precise result).
It's written as:

$$dA = x^2dx$$
From here we have:
$${dA\over dx} = x^2$$
It's derivative guys!
When I was working with it I couldn't even imagine that it can have such a backstory

![[Pasted image 20240407161936.png]]

___
By the way.
I've never mentioned it in Linear Algebra course by 3b1b, but Grant is just the best teacher I've ever seen. Thanks for awesome work!

<iframe width="560" height="315" src="https://www.youtube.com/embed/U_6AYX42gkU?si=hQs0VJj_mKu1RFMh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


