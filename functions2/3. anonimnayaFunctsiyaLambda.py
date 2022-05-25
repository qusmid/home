product = lambda x, y: x * y


print(product(2, 3))
print(type(product))

power = lambda x=1, y=2: x ** y
square = power
print(square(5))