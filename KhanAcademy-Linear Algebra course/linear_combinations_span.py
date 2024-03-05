# ther was not much things to discuss in previous videos
# as I've already known it from 3b1b, but here are some things I can do with python
# so here it is


# linear combinations:


def linear_combinations_scratch(v_factor, v, w_factor, w):
    assert len(v) == len(w)
    v = list(map(lambda x: x * v_factor, v))
    w = list(map(lambda x: x * w_factor, w))

    sum_ = []
    sub_ = []


    for i in range(len(v)):
        sum_.append(v[i] + w[i])
        sub_.append(v[i] - w[i])
    return sum_, sub_


a = [1, 2]
b = [0, 3]

print(linear_combinations_scratch(3, a, 2, b))

# and yeah. as it was mentioned in 3b1b course
# span is a set of all those vectors, that could be created