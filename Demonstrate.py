class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Iterating using a for loop
print("Custom Iterator Output:")
my_counter = Counter(1, 5)
for num in my_counter:
    print(num)

# Manual iteration using next()
it = iter(Counter(10, 12))
print("Manual Next:", next(it))
print("Manual Next:", next(it))