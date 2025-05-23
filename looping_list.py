letters = ["a", "b", "c", "d"]
letters.append("e")
letters.insert(0,"-")

letters.pop(0)
letters.remove("b")
del letters[3]

print(letters)  # Output: ['a', 'b', 'c', 'd',