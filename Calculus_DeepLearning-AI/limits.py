def function(x, hole):
    if x != hole:
        return x ** 2
    else:
        return x


def limit_approximation(func, hole):
    x = func(hole + 0.00001, hole)
    x1 = func(hole - 0.00001, hole)
    return f'with limit of {hole}: {x}, {x1}, but still not {hole ** 2}'


print(limit_approximation(function, 2))
