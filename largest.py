nums = [12, 45, 2, 41, 31, 10, 8, 6, 4]
largest = second_largest = float('-inf')
smallest = second_smallest = float('inf')

for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest:
        second_largest = n
        
    if n < smallest:
        second_smallest = smallest
        smallest = n
    elif n < second_smallest:
        second_smallest = n

print(f"2nd Largest: {second_largest}, 2nd Smallest: {second_smallest}")