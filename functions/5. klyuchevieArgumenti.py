def keyword_function(a=1, b=2):
    return a + b

print(keyword_function(b=4, a=5))
print(keyword_function())

def mixed_function(a, b=2, c=3):
    return a + b + c

# mixed_function(b=4, c=5) - ошибка, нет первого ключевого аргумента
print(mixed_function(1, b=4, c=5))
print(mixed_function(1))