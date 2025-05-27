items = [
    ("Product1", 10),
    ("Product2", 100),
    ("Product3", 15),
    ("Product4", 50),
    ("Product5", 90),
]

prices = []
for item in items:
    prices.append(item[1])

x = list(map(lambda item:item[1], items))

print(x)

print(prices)