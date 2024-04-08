# Essence of Calculus 2
Today I'm studying Essence of Calculus 2:
Topics: #Math #Math #MathForML #3b1b #calculus
Course:  [Essence of Linear Algebra by 3b1b](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
Progress: I have a lot of free time now (doom music)!
___
Notes:

Derivatives...
Ahh! What a wonderful topic I thought...
Actually things are deeper than they were explained.

For example:

Imagine car movement:

<iframe src='https://3b1b-posts.us-east-1.linodeobjects.com/content/lessons/2017/derivatives/figure-1.08-1.21.mp4#t=0.001'></iframe>
<iframe src='https://3b1b-posts.us-east-1.linodeobjects.com/content/lessons/2017/derivatives/figure-1.25-1.35.mp4#t=0.001'></iframe>

Now interesting quesion:
"How does velocity graph depend on this graph"

<img src='https://www.3blue1brown.com/content/lessons/2017/derivatives/figure-4.14.svg' width=60%>

At some reeeeeeeeaaaaaaally precise time slice:
$$dt \rightarrow 0$$
dt tends to be zero (but it's not zero)
___
Then at this point we can consider speed:

$$\vec v = {ds(t) \over dt}$$

For example $ds(t) = t^3$

Then our computation will look like:

![[Pasted image 20240408094223.png]]

![[Pasted image 20240408094235.png]]

![[Pasted image 20240408094252.png]]

![[Pasted image 20240408094307.png]]

As $dt \rightarrow 0$ we get:

$${ds\over dt}(2) = 3(2)^2$$

So, in such way we can compute velocity at some special time:
for example veloctity at $t=3s$:

$${ds\over dt}(3) = 3(3)^2 = 27m/s$$
___
Concept of derivative is really important, as by approximation it can turn mess into clean solution:

![[Pasted image 20240408094651.png]]

![[Pasted image 20240408094704.png]]

BUT IT'S JUST PARADOX PART HERE!

The thing is that we take our time as a number (In example I picked 3 sec)
But the truth is there's no movement in frozen on 3sec time. So despite we take 3sec, and it may sound wrong, we actually work with really precise pair of numbers:
3 and 3.0000001 for example.

There's even better example:
Does car move at $t=0$?
Well, the answer by formula is NO

$${ds \over dt}(0) = 3(0)^2 = 0m/s$$
But when does it start movement?
Question is not really good, cuz picking some approximate value will give us some value VEEERY close to 0, but not equal to it, meaning our speed is not 0.

That's a paradox that sound like some creepy math.

<img src='https://i.imgflip.com/278xmg.jpg' width=30%>
___
Btw speed represents kind of slope graph here:
As our $ds \over dt$ represents slope of tangent line.
It's actually pretty logical to think about it:

When our slope is steep and positive - our velocity is increasing -> our s grows faster
When our slope is steep and negative - our velocity is decreasing -> our s slope is going down and our car is moving backwards.
When our slope is flat - our velocity is const -> our s grows linearly.
(or stays in place if our slope at 0)
