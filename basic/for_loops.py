balance = 100
times = 8
double = 4
print(f"start balance: ${balance} X{double} double  {times} times")
for number in range(1, times):
    balance *= double
    currency = "${:,}".format(balance)
    print(f"{number}:   {currency}")
