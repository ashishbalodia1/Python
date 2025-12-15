# def f(x=[]):
#     x.append(1)
#     return x

# print(f())
# print(f())

# def f(x=None):
#     if x is None:
#         x = []
#     x.append(1)
#     return x

# print(f())
# print(f())

def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

show(lr=0.01, epochs=10)

