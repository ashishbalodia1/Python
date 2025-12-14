#Q5. Loop Practice- Print numbers from 1 to 20, but skip the multiples of 3 using continue.


for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=' ')


# Output--> 1 2 4 5 7 8 10 11 13 14 16 17 19 20 