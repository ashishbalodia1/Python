# # Q1. Assignment 1 — List Logic Write a function:
# # Input: list of integers
# # Output: new list containing only unique elements (preserve order)
# # ❌ Do NOT use set directly.


# def unique_elements(input_list):
#     unique_list = []
#     for item in input_list:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list

# # code for input list
# input_list = [1, 2, 2, 3, 4, 4, 5]
# # calling the function and printing the result  
# result = unique_elements(input_list)
# print(result)  # Output: [1, 2, 3, 4,



# Q2. Assignment 2 — Dictionary Problem
# Input: data = ["cat", "dog", "cat", "bird", "dog", "dog"]
# Output: {"cat": 2, "dog": 3, "bird": 1}

# input=["cat", "dog", "cat", "bird", "dog", "dog"]
# freq={}
# for x in input:
#     freq[x] = freq.get(x, 0) + 1

# print(freq)


# Q3. Assignment 3 — Set Logic ->Given two lists:
# a = [1,2,3,4]
# b = [3,4,5,6]
# Find:
# 1. Common elements
# 2. Elements only in a
# 3. Elements only in b

# a = [1,2,3,4]
# b = [3,4,5,6]
# print("Common in set a and set: ", list(set(a).intersection(set(b))))
# print("Element only in a: ", list(set(a).difference(set(b))))
# print("Element only in b: ", list(set(b).difference(set(a))))

# Q4. Assignment 4 — String Processing (Real ML Task)->Write a function that:
# 1. Takes a sentence
# 2. Converts to lowercase
# 3. Removes punctuation
# 4. Returns a list of words
# Example: "AI, ML is AWESOME!" → ["ai", "ml", "is", "awesome"]

import string


def str_processing(str1):
    # Convert to lowercase
    lowered = str1.lower()
    
    # Using translate for efficient character removal instead of manual loops
    translator = str.maketrans("", "", string.punctuation)
    cleaned = lowered.translate(translator)
    return cleaned.split()


str1 = "AI, ML is AWESOME!"
print(str_processing(str1))