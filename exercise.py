import math


#write unittests for the following function and name your file test_exercise.py , run your tests using python3 -m unittest test_exercise.py
def square(x):
    return x**2


def counter():
    name="Zanny"
    length_name = name.count()
    return length_name


def email():
    user_name = input("Name: ")

    return f"{user_name}.wethinkcode.com"


def square_root(y):
    
    if y < 0 :
        raise ValueError
    else:
        root = math.sqrt(y)
    return root
    

