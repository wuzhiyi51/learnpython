# coding:utf-8

'''
我们有一个包含N个元素的元组或序列，现在想把它分解为N个单独的变量。

例如我们有一个序列[1, 2, 3]，想把1, 2, 3分别赋值给a, b, c三个变量。

解决方案
只需要简单的赋值就可以了，唯一的要求是变量的数量和序列的数量必须要一致
'''

l = ['foo', 5, 'bar']
a,b,c=l
print(a,b,c)


t=(1,2,3)
f,d,e=t
print(f,d,e)


ls = [1,2,3]
i,j=ls
print(i,j)


def foo():
    for i range(3):
        yield i

x,y,z=foo()
print(x,y,z)