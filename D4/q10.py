# Data Normalizer class   (Yahi se reference lena hai->ye toh mene nhi kra hai )

class DataNormalizer:
    """
    A callable object to normalize input data using min-max scaling.
    """
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
        self.range = max_val - min_val

    def __call__(self, data_point):
        """
        Normalizes a single data point when the object is called.
        """
        if self.range == 0:
            return 0  # Avoid division by zero if all data is the same
        normalized_value = (data_point - self.min_val) / self.range
        return normalized_value

# --- Usage ---

# 1. Instantiate the object with the dataset's overall min and max values
#    (e.g., for a dataset where the lowest value is 10 and highest is 90)
normalizer = DataNormalizer(min_val=10, max_val=90)

# 2. Call the instance like a function to normalize specific data points
point1 = 20
point2 = 50
point3 = 90

print(f"Normalized value of {point1}: {normalizer(point1):.2f}")
print(f"Normalized value of {point2}: {normalizer(point2):.2f}")
print(f"Normalized value of {point3}: {normalizer(point3):.2f}")

# You can also use it in functions like map()
data_list = [10, 30, 70, 85, 50]
normalized_list = list(map(normalizer, data_list))
print(f"\nNormalized list: {normalized_list}")
