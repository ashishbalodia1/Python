# Q6. (Medium) — Polymorphism  Create two classes:
# LinearModel
# TreeModel
# Both must implement:

# def train(self):
    # pass

# Write a loop that calls train() without checking object type.
from ast import In


class LinearModel:
    def train(self):
        print("Training Linear Model...")

class TreeModel:
    def train(self):
        print("Training Tree model...")

models =[LinearModel(), TreeModel()]

for model in models:
    model.train()

# explaination:
# In this code, we define two classes, LinearModel and TreeModel, each implementing a train() method.
# We then create a list of model instances and iterate through them, 
# calling the train() method on each without checking their types.
# This demonstrates polymorphism, as both classes provide their own implementation of the train() method, 
# allowing us to treat them uniformly in the loop.
