import random
li = []

for i in range(random.randint(0, 24), random.randint(25, 50)):
    li.append(random.randint(0, 10))
print(li)

def for_function(li):
    summa_for = 0
    for i in li:
        summa_for += i
    return summa_for
def while_function(li):
    summa_while = 0
    q = 0
    while q < len(li):
        summa_while = summa_while + li[q]
        q += 1
    return summa_while
def recursed_function(li):

    if li == []:
        return 0
    else:
        summa = recursed_function(li[1:])
        summa = summa + li[0]
        return summa

summa_for = for_function(li)
print(f"Amount in for: {summa_for}")
summa_while = while_function(li)
print(f"Amount in while: {summa_while}")
summa = recursed_function(li)
print(f"Recursed amount: {summa}")
