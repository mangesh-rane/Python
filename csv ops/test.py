# import os
#
# class Adder(object):
#
#     def __init__(self, inputs):
#         self.inputs = inputs
#
#     def __call__(self):
#         return "You called object"
#
#
# adder_2 = Adder(2)
# adder_3 = Adder(3)
#
# print(adder_2())
#
# class Subs(object):
#
#     def __init__(self):
#         pass
#
# subs_1 = Subs()
# subs_2 = Subs()
#
# if not callable(subs_1):
#     print("Not Callable")
#
# from contextlib import contextmanager
#
# @contextmanager
# def fileManager(filename):
#
#     try:
#         f = open(filename)
#         print("getting file", filename)
#         yield f
#     except IOError:
#         pass
#     finally:
#         f.close()
#
# with fileManager("readme.txt") as f:
#     print(f.read())
#
# # using class
# class FileManager(object):
#
#     def __init__(self, filename):
#         self.filename = filename
#
#     def __enter__(self):
#         self.filea = open(self.filename)
#         return self.filea
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.filea.close()
#
# print("-" * 50 + "using class bases context manager")
# with FileManager("readme.txt") as f:
#     print(f.read())
#
# # closures
# def upper():
#
#     outer = "OUTER"
#     def inner():
#         print(outer)
#


# import logging
#
# logging.basicConfig(filename='example.log', level=logging.INFO)
#
#
# def logger(func):
#     def log_func(*args):
#         logging.info(
#             'Running "{}" with arguments {}'.format(func.__name__, args))
#         print(func(*args))
#
#     # Necessary for closure to work (returning WITHOUT parenthesis)
#     return log_func
#
#
# def add(x, y):
#     return x + y
#
#
# def sub(x, y):
#     return x - y
#
#
# add_logger = logger(add)
# sub_logger = logger(sub)
#
# add_logger(3, 3)
# add_logger(4, 5)
#
# sub_logger(10, 5)
# sub_logger(20, 10)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# late binding
# def log(name):
#
#     def inner():
#         print("asd" + name)
#     return inner
#
#
# l = log("test")
# print("--.")
# l()

# ---
# class Indenter(object):
#
#     def __init__(self):
#         self.space = 1
#
#     def __enter__(self):
#         self.space = self.space + 2
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.space -= 2
#
#     def pprint(self, name):
#         print(" " * self.space + name)
#
# with Indenter() as indent:
#     indent.pprint("Hello")
#     with indent:
#         indent.pprint("World")
#         with indent:
#             indent.pprint("indented")
#         with indent:
#             indent.pprint("qqweqwrqwr")
#     with indent:
#         indent.pprint("asdasdf")
# with indent:
#     indent.pprint("zxcv")
#
import binascii
from collections import deque


def encode(data, n):
    while n:
        data = binascii.hexlify(data.encode()).decode()
        n -= 1
    return data

def decode(data, n):
    while n:
        data = binascii.unhexlify(data.encode()).decode()
        n -= 1
    return data

with open("test.py") as f:
    data = f.read()
    data = encode(data, 5)

q = deque(list(data))
d = ''
order_l = []
char_l = []
while q:
    dp = q.popleft()
    if dp != d:
        d = dp
        char_l.append(dp)
        order_l.append(1)
    else:
        order_l[-1] = order_l[-1] + 1

char_l = [str(c) for c in char_l]
ch_l = ""
for i in char_l:
    ch_l += "".join(str(i))

or_l = ""
for i in order_l:
    or_l += "".join(str(i))

st = ch_l + "|" + or_l

data = ""
for char, multiplier in zip(char_l, order_l):
    data += str(char) * multiplier

data = decode(data, 5)

print("===>" + data)
