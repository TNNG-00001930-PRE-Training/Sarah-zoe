result = []

for num in range(1000, 3001):
    num_str = str(num)
    all_even = True
    for digit in num_str:
        # Check if the digit is odd
        if int(digit) % 2 != 0:
            all_even = False
            break
    if all_even:
        result.append(num)

print(','.join(map(str, result)))
