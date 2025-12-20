# “I hold state and behavior of the model.”
class Model():
    print("This is a model...")


    def __init__(self):
        self.trained=False

    def train(self, X,y):
        print("Training model on data...")
        self.trained=True