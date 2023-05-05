# Define a function
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


# Calls functions
# print_lyrics()
# repeat_lyrics()

# print(type(print_lyrics))  # <class 'function'>
# -----------------------------------------------------------------------

"""
Parameters and arguments
"""


def print_twice(bruce):
    print(bruce)
    print(bruce)


# print_twice('Spam')
# print_twice('Spam ' * 4)

# result = print_twice('Spam')
# print(result)
# print(type(None))

"""
To return a result from a function, we use the return statement in our function
"""


def addtwo(a, b):
    return a + b


print(addtwo(1, 2))




