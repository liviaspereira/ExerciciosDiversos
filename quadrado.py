def sum_square(numbers):
    sum_square = 0
    for number in numbers:
        sum_square += number ** 2
    return sum_square

print(sum_square([1,2]))