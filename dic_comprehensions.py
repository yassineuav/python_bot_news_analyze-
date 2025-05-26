values = []
b = 1
for x in range(1, 10):
    b *= 2
    values.append(b)
    
print(values)

values = {x*2 for x in range(10)}
print(values)