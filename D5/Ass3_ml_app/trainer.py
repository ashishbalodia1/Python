# “I know how to train a model using data.”
class Trainer():

    def __init__(self, model, dataloader):
        self.model=model
        self.dataloader=dataloader()

    def run(self):
        X,y =self.dataloader.load_data()
        self.model.train(X,y)
        print("Training completed")