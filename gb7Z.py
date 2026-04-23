data = [10, 10.5, "Hello", [1, 2], (3, 4), {5, 6}, {"a": 1}, True, complex(2, 3)]
for item in data:
    print(f"Value: {item} | Type: {type(item)} | Memory Address: {id(item)}")