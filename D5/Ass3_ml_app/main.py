# “I wire everything together.”
from model import Model
from trainer import Trainer
from data_loader import DataLoader

def main():
    dataloader=DataLoader
    model=Model()
    trainer=Trainer(model, dataloader)

    trainer.run()

if __name__=="__main__":
    main()