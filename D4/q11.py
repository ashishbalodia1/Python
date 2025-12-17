# Q10. (Advanced — ML SYSTEM DESIGN)
# Design a mini ML pipeline using OOP with:
# Classes:
# DataLoader
# Model
# Trainer
# Evaluator

# Requirements:
# No global variables
# Loose coupling
# Polymorphic Model


class DataLoader:
    def load_data(self):
        X=[1,2,3,4]
        y=[2,4,6,8]
        return X,y

class Model:
    def train(self, X, y):
        self.weight=sum(y)/sum(X)

    def predict(self, x):
        return self.weight * x
    
class Trainer:
    def __init__(self, model, dataloader):
        self.model=model
        self.X, self.y = dataloader.load_data()
    
    def run(self):
        self.model.train(self.X, self.y)

class Evaluator:
    def evaluate(self, model, X, y):
        correct=0
        for xi, yi in zip(X,y):
            if model.predict(xi)==yi:
                correct+=1
        return correct/len(y)
    
dataloader= DataLoader()
model=Model()
trainer=Trainer(model, dataloader)
trainer.run()

evaluator = Evaluator()
accuracy= evaluator.evaluate(model, *dataloader.load_data())
print("Accuracy: ", accuracy)

