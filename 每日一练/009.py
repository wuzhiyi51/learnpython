#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   009.py
@Time    :   2019/07/04 17:17:39
@Author  :   Wu ZhiYi 
@Version :   1.0
@Contact :   wuzhiyi51@gmail.com
@License :   (C)Copyright 2019-20120, wuzhiyi
@Desc    :   None
'''

# here put the import lib

# yield 用法,yield 

def foo():
    print("starting......")
    while True:
        res = yield 4
        print("res: ", res)
g=foo()
print(next(g))
print('*'*20)
print(next(g))


#生成器是一种只能迭代一次的迭代器，生成器不会一次将所有的元素存入内存中，而是一边迭代一边运算：
print('*'*20)
mygenerator=(x*x for x in range(3))
for i in mygenerator:
    print(i)



#yield的使用和return的使用没什么区别，只是yield会返回一个生成器
def createGenerator():
    mylist=range(3)
    for i in mylist:
        yield i*i
mygen=createGenerator()
print(mygen)#对象

for i in mygen:
    print(i)


#当你的函数需要返回一个很大的元素集合，并且每个元素只需要用到一次的时候，使用yield会非常方便
#要想理解yield，你必须理解当你调用一个包含yield的函数的时候，函数体代码并不会执行，这个函数仅仅是返回一个生成器而已
'''
当你第一次向后迭代（用next或for...in...语句时）这个生成器时，函数体才会从最开始执行到yield处然后返回yield的值，随后再次向后迭代，会执行剩余的代码然后再次遇到yield停止并返回值。直到运行到函数结尾处停止，此时如果是用next()则会抛出StopIteration异常，如果是用for...in...则会结束循环并且不会有异常
'''

def createGenerators():
    print('head')
    for i in range(5):
        yield i*i
    print('tail')
print(createGenerators())
g=createGenerators()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))