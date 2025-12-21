# Assignment 5 — ML-Style Validation
# Write a function:

# def train(X, y):

# Rules:
# Assert X and y are same length
# Raise error if empty
# Print "Training started" if valid


def train(X,y):
    try:
        if len(X)==0 or len(y)==0:
            raise ValueError("Training data can't be empty")
        elif len(X)!=len(y):
            raise ValueError("X and y must be of same length")

    except Exception as ex:
        print(ex)

    else:
        print("Training started!")
    
    finally:
        print("Program executed successfully")

X=int(input("Enter value of X: "))
y=int(input("Enter value of y: "))

train(X, y)


# METHOD 2:
def train(X, y):
    if len(X) == 0 or len(y) == 0:
        raise ValueError("Training data cannot be empty")

    if len(X) != len(y):
        raise ValueError("X and y must be of the same length")

    print("Training started")


# Example usage
X = [1, 2, 3]
y = [2, 4, 6]

train(X, y)
