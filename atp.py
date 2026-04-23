s = input("Enter string: ")
v, c, d, sp = 0, 0, 0, 0
for char in s.lower():
    if char.isdigit(): d += 1
    elif char in 'aeiou': v += 1
    elif char.isalpha(): c += 1
    else: sp += 1
print(f"Vowels: {v}, Consonants: {c}, Digits: {d}, Special: {sp}")