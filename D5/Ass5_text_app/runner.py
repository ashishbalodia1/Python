# “I run the pipeline.”
class Runner:
    def __init__(self, loader, processor):
        self.loader=loader
        self.processor=processor

    def run(self):
        text=self.loader.load_text()
        result = self.processor.process(text)
        print("Processing completed")
        return result