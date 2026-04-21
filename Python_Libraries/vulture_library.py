import os
import pandas as pd
import numpy as np

class Greeter:
    def greet(self):
        print("Hi")


def hello_world():
    v=12
    v2=32+2
    v3="ashish"
    message="hello world"
    greeter=Greeter()
    greet_func = getattr(greeter, "greet")
    greet_func()


if __name__ == '__main__':
    hello_workd()