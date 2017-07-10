#一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
#第一种方法
fib = lambda n: n if n <= 2 else fib(n-1)+fib(n-2)

#第二种方法
def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
    return b

#第三种方法
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
@ memo
def fib(i):
    if i < 2:
        return 1
    return fib(i-1)+fib(i-2)

#一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
fib = lambda n : n if n < 2 else 2*fib(n-1)
#矩形覆盖问题
fib = lambda n: n if n <= 2 else fib(n-1)+fib(n-2)