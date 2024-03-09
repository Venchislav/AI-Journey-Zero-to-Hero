"""
If we have some set of vectors V
it will be a linear subspace if it follows 3 conditions:
1. It includes zero vector (0; 0) for R2 (0; 0; 0) for R3 and (0; ...; 0) for Rn
2. It is closed under scalar multiplication (meaning if we multiply any vector v by any real number c and get vector x)
Vector x will be in subspace
Note. It's pretty logical to include zero vector, as we can choose c = 0  =>  zero vector must be in V

3. It is closed under addition (meaning any vector v1 + any other vector v2 resulting v3 in case that v3 also in V)

---------------------------------------------------------------

Here's an interesting question:  Is V = {[0; 0]} a subspace of R2 ?

Well, let's see:

1. Does it contain zero vector: for sure ✅
2. Is it closed under scalar mul: well let's take c=666: 666 * [0; 0] = [0; 0], which is in V, so it's also true✅
3. Is it closed under addition: well if we take [0; 0] and [0; 0] (as we have nothing else) [0; 0] + [0; 0] = [0; 0]
It's in V, so it's also a linear subspace! ✅
"""


