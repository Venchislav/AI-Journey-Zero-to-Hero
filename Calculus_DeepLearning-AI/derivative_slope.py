"""
Derivative - pretty important concept of calculus.
It describes how fast function changes (and how it changes at all)

if we have some plot with, idk... normal distribution:
we'll be able to draw a special line describing how function changes at each point...

But what slope to choose?

Slope is calculated as "Rise over Run"
Rise is our vertical delta, while run is our horizontal delta

Here's fancy python example
"""
import random


def simple_parabola(x):
    return x ** 2


def rise_over_run(function):
    run = random.randint(0, 10)
    rise = function(run)

    return rise / run


print(rise_over_run(simple_parabola))

# cool
# but wrong...
