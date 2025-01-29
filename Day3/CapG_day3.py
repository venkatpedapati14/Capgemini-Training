L1 = []
print("1. An empty list:", L1)

L2 = [0, 1, 2, 3]
print("2. List with four items:", L2)

L3 = ['abc', ['def', 'ghi']]
print("3. A nested list:", L3)

L4 = list('spam')
print("4. List created from string 'spam':", L4)

L5 = list(range(-4, 4))
print("5. List created from range(-4 4):", L5)

L6 = [10, 20, 30, 40]
print("6. Element at index 2 of L6:", L6[2])

L7 = ['x', [10, 20, 30], 'y']
print("7. Element at L7[1][2] (nested list):", L7[1][2])

L8 = [0, 1, 2, 3, 4, 5]
print("8. Slicing L8 from index 2 to 4 (L8[2:5]):", L8[2:5])

print("9. Length of L8:", len(L8))

L9 = [10, [100, 200, 300, 400], 50]
print("10. Element at L9[1]:", L9[1])

print("\nSummary of Lists:")
print("L1:", L1)
print("L2:", L2)
print("L3:", L3)
print("L4:", L4)
print("L5:", L5)
print("L6:", L6)
print("L7:", L7)
print("L8:", L8)
print("L9:", L9)
