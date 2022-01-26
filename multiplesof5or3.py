sum = 0

for multiple in range(1000):
    if multiple % 3 == 0 or multiple % 5 == 0:
        sum += multiple
print(sum)