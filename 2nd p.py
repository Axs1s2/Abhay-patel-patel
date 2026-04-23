# Immutable (Cannot change)
x = 10
print(f"Original Int Address: {id(x)}")
x += 1
print(f"New Int Address: {id(x)}") # Address changes

# Mutable (Can change)
L = [1, 2]
print(f"Original List Address: {id(L)}")
L.append(3)
print(f"Same List Address: {id(L)}") # Address stays same