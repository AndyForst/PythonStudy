# 连乘
from functools import reduce
def prod(L):
    def product(x,y):
        return x * y
    return reduce(product, L)
if __name__ == '__main__':
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))