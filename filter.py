def my_map(func, iterable):
    return [func(x) for x in iterable]

def my_filter(func, iterable):
    return [x for x in iterable if func(x)]

def my_reduce(func, iterable):
    res = iterable[0]
    for x in iterable[1:]:
        res = func(res, x)
    return res

nums = [1, 2, 3, 4]
print(my_map(lambda x: x*2, nums))
print(my_filter(lambda x: x>2, nums))
print(my_reduce(lambda x, y: x+y, nums))