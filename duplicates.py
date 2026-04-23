def remove_dup(L):
    seen = []
    for x in L:
        if x not in seen:
            seen.append(x)
    return seen
print(remove_dup([1, 2, 2, 3, 1, 4]))