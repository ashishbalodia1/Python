# Q16. Build your own range()-->Write a function:
# def my_range(start, stop, step):
    # ...
# Which behaves like Python’s range() and returns a list.

def my_range(start, stop, step):
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

print(my_range(1, 10, 2))



# Outout: [1, 3, 5, 7, 9]