items = [
    ("Product1", 10),
    ("Product2", 100),
    ("Product3", 15),
    ("Product4", 50),
    ("Product5", 90),
]

items.sort(key=lambda item:item[0])
print(items)



def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)