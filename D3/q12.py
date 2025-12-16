# Q12. Find Duplicate Using Set -> Return the first duplicate encountered.

seen = set()
for x in [1,2,3,2,4]:
    if x in seen:
        print(x)
        break
    seen.add(x)
