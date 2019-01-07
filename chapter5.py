# -*- coding: utf-8 -*-
def factorial(n):
    """ return n!"""
    return 1 if n<2 else n*factorial(n-1)


fruits = ['apple', 'banana', 'strawbarry']

class aa:
    def __init__(self,name):
        self._name = name
    def get_name(self):
        return "name is " + self._name
    def __call__(self, *args, **kwargs):
        return self.get_name()


def tag(name, *content, **attrs):
    """生成一个或多个htnl标签"""

    if attrs:
        attr_str = ''.join(' %s="%s"'%(attr, value)for attr,value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>'%(name, attr_str, c, name) for c in content)
    else:
        return '<%s%s/>'% (name, attr_str)
if __name__ == '__main__':
    print(factorial(3))
    print(help(factorial))
    print(type(factorial))
    print(sorted(fruits, key=len))
    print(dir(factorial))
    tom = aa('tom')
    print(tom())

    print(tag('p','hello', id=33))
