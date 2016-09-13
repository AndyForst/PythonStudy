# 字母标准化
def standard(s):
    s = s.lower()
    t = s[0].upper()
    t = t + s[1:]
    return t

if __name__ == '__main__':
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(standard, L1))
    print(L2)
    L3 = list(map(lambda x:x.capitalize(), L1))
    print(L3)
