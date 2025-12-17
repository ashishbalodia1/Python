# Q9. (Advanced) — Callable Object
# Create a class Scaler:
# initialized with mean and std
# make the object callable to normalize input data
# Usage:
# s = Scaler(10, 2)
# s(14)  # output: 2

class Scalar:
    def __init__(self, mean, std):  
        self.mean=mean
        self.std=std

    def __call__(self, data_point):
        normalized_value=( data_point - self.mean)/ self.std
        print(normalized_value)
        

    
s=Scalar(10,2)
s(14)