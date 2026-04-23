# 1. Manual Map
def my_map(func, iterable):
    return [func(x) for x in iterable]

# 2. Manual Filter
def my_filter(func, iterable):
    return [x for x in iterable if func(x)]

# 3. Manual Reduce
def my_reduce(func, iterable):
    it = iter(iterable)
    value = next(it)
    for x in it:
        value = func(value, x)
    return value

# Testing
nums = [1, 2, 3, 4, 5]
print("Map (Squares):", my_map(lambda x: x**2, nums))
print("Filter (Even):", my_filter(lambda x: x % 2 == 0, nums))
print("Reduce (Sum):", my_reduce(lambda x, y: x + y, nums))