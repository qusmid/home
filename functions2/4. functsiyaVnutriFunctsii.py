def mul(a):
    def helper(b):
        return a * b

    return helper


print(mul(3)(2))

three_mul = mul(3)
print(three_mul(5))
