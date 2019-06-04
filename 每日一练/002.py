# coding:utf-8

# 如何序列化输出元素包含字符串元组的字符串元组,  将zoo2输出为python, monkey, elephant

zoo1 = ('monkey', 'elephant')
zoo2=('python', zoo1)

print(zoo2)


zoo1 = ('monkey', 'elephant')
zoo2 = ('python', *zoo1)
s = ', '.join(zoo2)
print(s)



zoo = (
    'monkey',
    'elephant',
    ('penguin', 'camel'),
    ('zebra', 'giraffe'),
    'python',
)
def my_join(tpl, sep):
    return sep.join(x if isinstance(x, str) else my_join(x, sep) for x in tpl)
print(my_join(zoo, ', '))