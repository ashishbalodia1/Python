# “I connect everything.”
from text_loader import TextLoader
from processor import TextProcessor
from runner import Runner

def main():
    loader=TextLoader()
    processor=TextProcessor()
    runner=Runner(loader, processor)

    result= runner.run()
    print("Final Result: ", result)

if __name__=="__main__":
    main()