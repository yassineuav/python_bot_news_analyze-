balance = 1000
print(f"weeks \t\t seed:{balance}    (X4 for 5 times)" )

for i in range(1, 6):
    balance *= 4
    # gain = format("%f.",balance)
    result = "${:,}".format(balance)
    print(f"  {i} \t\t {result}  \t\t 400%")
    
