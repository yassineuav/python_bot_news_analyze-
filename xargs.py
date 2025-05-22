def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(3, 4, 2, 2, 5, 4))