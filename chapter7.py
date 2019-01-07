# -*- coding: utf-8 -*-


def deco(func):
    def inner():
        print('running inner()')
    return inner
@deco
def target():
    print('running target()')




registry = []
def register(func):
    print('running register(%s)'%func)
    registry.append(func)
    return func
@register
def f1():
    print('running f1()')
@register
def f2():
    print('running f2()')


class order:
    def __init__(self, fidelity, total):
        self.fidelity = fidelity
        self.total = total
promos = []
def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    return order.total*0.05 if order.fidelity >= 1000 else 0
@promotion
def once_reduce(order):
    return 300 if order.total>1000 else 0
@promotion
def cut(order):
    return order.total * 0.1
def best_promo(order):
    return max(promo(order) for promo in promos)



class Averager():
    def __init__(self):
        self.series = []
    def __call__(self, new_value):
        self.series.append(new_value)
        return sum(self.series)/len(self.series)
def make_averager():
    series = []
    #a = 0
    def averager(new_value):
        #a +=1
        series.append(new_value)
        return sum(series)/len(series)
    return averager

from functools import wraps

import time
def clock1(func):
    @wraps(func)
    def clocked(*args):
        t0 = time.time()
        result = func(*args)
        user_time = time.time()-t0
        name = func.__name__
        print('[%0.8fs]%s -> %r'%(user_time, name, result))
        return result
    return clocked
@clock1
def snooze(seconds):
    time.sleep(seconds)
    return 'aa' + str(seconds)
@clock1
def fibonacci(n):
    return 1 if n < 2 else n*fibonacci(n-1)

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def decorate(func):
    print('decorate')
    print(func)
    def clocked(*_args):
        print('----')
        print(_args)
        t0 = time.time()
        print(func.__name__)
        _result = func(*_args)
        elapsed = time.time() - t0
        name = func.__name__
        args = ', '.join(repr(arg) for arg in _args)
        result = repr(_result)
        print(DEFAULT_FMT.format(**locals()))
        return _result
    return clocked

def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        print('decorate')
        print(func)
        @wraps(func)
        def clocked(*_args):
            print('----')
            print(_args)
            t0 = time.time()
            print(func.__name__)
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate
@clock()#注意：带参数的有括号
def snooze1(seconds):
    print('snoozee1')
    time.sleep(seconds)
@decorate
def snooze2(seconds):
    print('snoozee2')
    time.sleep(seconds)
def outer(flag):  # step 2
    def wrapper(func):  # step 4
        print(func)
        def inner(*args, **kwargs):  # stpe 6
            if flag:  # step 9
                print('before')  # step 10
                ret = func(*args, **kwargs)  # step 11  执行原函数
                print('after')  # step13
            else:
                ret = func(*args, **kwargs)
                print('123')
            return ret  # step 14
        return inner  # step 7
    return wrapper  # step 5

def get_sum(initial_sum):
    def avg(count):
        initial_sum[0] += count
        return initial_sum[0]
    return avg
if __name__ == '__main__':
    avg = get_sum([0])
    print(avg(1))
    print(avg(2))
    print(avg(4))
    #target()
    #print(target)
    #print('running main()')
    #print('registry ->', registry)
    #f1()
    #f2()
    #print(promos)
    #print(best_promo(order(999,1000)))
    #avg1 = Averager()
    #avg2 = make_averager()
    #print(avg1(10))
    #print(avg1(20))
    #print(avg1(30))
    #print(avg2(10))
    #print(avg2(20))
    #print(avg2(30))
    #print(avg2.__code__.co_varnames)
    #print(avg2.__code__.co_freevars)
    #snooze(2)
    #print(snooze.__name__)
    #fibonacci(300)

    print('main')
    print(snooze1.__name__)
    print(snooze2.__name__)
    snooze1(2)
    snooze2(3)
    F = True  # step 1 装饰器的开关变量

    @outer(F)  # 先执行step 3 ：outer(True)这个函数，然后step 6：@wrapper   #此处把开关参数传递给装饰器函数
    def hahaha():
        pass  # step 12
    hahaha()  # step 8    相当于inner()