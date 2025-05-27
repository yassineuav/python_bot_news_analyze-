items = [
    ("Product1", 10),
    ("Product2", 100),
    ("Product3", 15),
    ("Product4", 50),
    ("Product4", 5),
    ("Product5", 90),
]


# x = list(filter(lambda item: item[1]>=10, items))
x = [item for item in items if item[1] >= 10]
print(x)


prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]

