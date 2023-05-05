# name = input()
# age = input()
# print(name + ' is ' + age)

# num = int(input())
# print(num)

# # Walrus operator
# print(num := int(input()))
# print(num + 1)

# x = int(input())
# y = int(input())
# print(x + y)

# a = 438
# b = 636
# add = a + b
# sub = a - b
# mul = a * b
# div = a / b
# print("a + b = " + str(add))
# print("a - b = " + str(sub))
# print("a * b = " + str(mul))
# print("a / b = " + str(div))

"""
Write a program that takes two integers x and y from the user and checks if x is greater than y.
If x is greater than y, print "x > y: True" on the screen,
if x is less than y, print "x > y: False" on the screen.
"""
# x = int(input())
# y = int(input())
#
# if x > y:
#     print('x > y: True')
# else:
#     print('x > y: False')

# a = int(input())
# Total = int(input())
#
# Total += a  # Using += Operator
# print('The Value of the Total after using += Operator is:', Total)
# Total -= a  # Using -= Operator
# print('The Value of the Total after using -= Operator is:', Total)
# Total *= a  # Using *= Operator
# print('The Value of the Total after using *= Operator is:', Total)
# Total //= a  # Using //= Operator
# print('The Value of the Total after using //= Operator is:', Total)
# Total **= a  # Using **= Operator
# print('The Value of the Total after using **= Operator is:', Total)
# Total /= a  # Using /= Operator
# print('The Value of the Total after using /= Operator is:', Total)
# Total %= a  # Using %= Operator
# print('The Value of the Total after using %= Operator is:', Total)

x = int(input())
y = int(input())
z = int(input())
t = int(input())

print("Result evaluation is", (x > y) and (z < t))
