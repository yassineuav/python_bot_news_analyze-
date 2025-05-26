# point = { "x":1, "y":2}
point = dict(x=1, y=2)
print(point.get("xx", "none"))

for key, value in point.items():
    print(key, value)