numbers = []
CRED = '\033[31m'
CGRN = '\033[32m'
CEND = '\033[0m'

def get_value(msg):
    while True:
        try:
            value = int(input(msg))
        except:
            print('{}Input integer digit only!{}'.format(CRED,CEND))
            continue
        else:
            return value
            break

#fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1

def SubFib(startNumber, endNumber):
    for cur in f():
        if cur > endNumber: return
        if cur >= startNumber:
            yield cur

for i in SubFib(10, 200):
    print(i)