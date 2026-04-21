def maxNum(numbers):
    max_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i

    return max_num