successfull = True
for number in range(1, 3):
    print(f"{number} Attempt")
    if successfull:
        print("Successfull")
        break
else:
    print("attempted 3 times and faild")
    