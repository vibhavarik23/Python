import logging

logging.basicConfig(filename='test1.log',level=logging.DEBUG, format='%(asctime)s-%(module)s-%(funcName)s-%(lineno)d-%(levelname)s-%(message)s')


def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b


a=int(input("a="))
b=int(input("b="))

s=add(a,b)
logging.debug(s)

m=subtract(a,b)
logging.debug(m)

p=multiply(a,b)
logging.debug(p)

d=divide(a,b)
logging.debug(d)