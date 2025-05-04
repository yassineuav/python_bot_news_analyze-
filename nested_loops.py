times = 7
for x in range(2):
    for y in range(2):
        for z in range(2):
            
            print(f"{times} {"-|" if times > 0 else "_ "*16}")
            times -= 1