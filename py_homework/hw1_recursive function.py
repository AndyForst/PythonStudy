# 汉诺塔
def move(n,a,b,c):
    if n==1:
        print(a,'to',c)
        return
    move(n-1,a,c,b)
    print(a,'to',c)
    move(n-1,b,a,c)
    return
move(3,'A','B','C')
