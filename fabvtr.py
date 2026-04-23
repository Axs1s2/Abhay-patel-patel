# With Slicing
s = input("Enter: ")
print("Palindrome" if s == s[::-1] else "Not Palindrome")

# Without Slicing
rev = ""
for i in range(len(s)-1, -1, -1):
    rev += s[i]
print("Palindrome" if s == rev else "Not Palindrome")