#uebung 1

def after5(func):
    def wrapper(*args,** kw):
        wrapper.count1 +=1
        if wrapper.count1 == 5:
            return func(*args,** kw)
    wrapper.count1 = 0
    return wrapper


@after5
def doit(): print("Yo!")

doit()
doit()
doit()
doit()
doit()
#uebung 2
n=10

def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)#先给x=10 分配地址，然后一直分配算到1. 但是f(2)这时候的max(memo.keys())是2而非10.
        if x == n:  #key_name = max(my_dict, key=my_dict.get) 得到最大value的key dict.key()返回所有的key
            print(memo[x])
            #print(max(memo.keys()))
        return memo[x]

    return helper


@memoize
def fib(n):
    print("fib({})".format(n))   #print("{} {}".format("hello","world") )
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(10)

#uebung 3
#generator


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

print([i for i in fibon(10)])

#uebung 4
# make sure function can only be called with a float and an int
def accepts(*type):
    def decorator(fun):
        def wrapper(*args,**kw):
            for i in args:
                if not isinstance(i, type):
                    print(i)
                    raise AssertionError("type wrong") #
        return wrapper

    return decorator

@accepts(float, int)
def pow(base, exp):
  pass

# raise AssertionError
pow('x', 10,[1,2,3])

