import random

"""
The function random returns a random float between 0.0 and 1.0 (including 0.0 but not 1.0) 
"""
# for i in range(10):
#     print(random.random())

"""
The function randint takes the parameters low and high,
and returns an integer between low and high (including both)
"""
# print(random.randint(5, 10))

"""
To choose an element from a sequence at random, you can use choice:
"""
t = [1, 2, 3]
print(random.choice(t))
