try:
    numbers = [1,2,3]
    print(numbers[24])
    xfactor = 10/ 0
except (IndexError, ZeroDivisionError) as e:
    print(f" exception throw {e}")

else :
    print("NO exception were thrown")
finally:
    pass