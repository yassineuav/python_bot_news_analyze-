# list unpacking
numbers = list(range(1, 5))

first, second, third, *others = numbers

print(f"{first}, {second}, {third}, {others}")
print(numbers)  