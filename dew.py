#!/usr/bin/python3


def main():
    print(A.__bases__)
    a = A()
    a.remove(2)
    print(a.v, a.xx)
    a.xx = 1
    c = C()
    c.append(1)
    print(c.v)
    print(isinstance(a, C), isinstance(a, B), type(a))
    print(a.__dict__)
    print(A.__dict__)
    try:
        x = 1/1
    except ZeroDivisionError as e:
        print(e)
    else:
        print(x)
    finally:
        print('HaHa')
    s = Sd()
    s.lst = [1, 3, 2]
    s[1] = '123'
    print(s)
    print(s.lst)
    print(repr(s))
    print(s[-1], s[:], len(s))
    # print(s.pp,s.__dict__)
    s.sss = 123
    s.__dict__['fff'] = 123
    # print(s.pp,s.__dict__)


class B:
    def __init__(self):
        self.v = [2]

    def remove(self, value):
        self.v.remove(value)

    def append(self, v):
        self.v.append(v)


class C:
    xx = 1

    def __init__(self):
        self.v = [1, 2, 3]

    def append(self, v):
        self.v.append(v)


class A(C, B):
    def remove(self, value):
        super().remove(value)
        self.append(value)


def check_index(key):
    print(key)
    if not isinstance(key, (int, str, slice)):
        raise TypeError


def f_getitem(self, key):
    check_index(key)
    return self.dit.get(key, None)


def f_setitem(self, key, value):
    check_index(key)
    self.dit[key] = value


def g_getitem(self, key):
    check_index(key)
    return self.lst[key]


def g_setitem(self, key, value):
    check_index(key)
    self.lst[key] = value


def func(*args, **kwargs):
    print(args, kwargs)


class SepicalDict:
    def __init__(self, dit=None):
        self.dit = dit

    __getitem__ = f_getitem
    __setitem__ = f_setitem

    def __repr__(self):
        return repr(self.dit)

    def __str__(self):
        return 'dawdled'

p = property


def g_getattribute(self, name):
    if name == 'pp':
        print('---------')
    elif name in ('__dict__', 'sss', 'fff'):
        print('{}  ddd!'.format(name))
    return super(Sd, self).__getattribute__(name)


def g_setattribute(self, name, value):
    """ a function linked to the method __setattr__ of class Sd.
    :param self: object itself
    :param name: attribute name
    :param value: attribute value to set
    :return: None.
    """
    print('******')
    super(Sd, self).__setattr__(name, value)


Sd = type('Sd', (), dict(
    lst=[],
    __getitem__=g_getitem,
    __setitem__=g_setitem,
    __len__=lambda self: len(self.lst),
    pp=p(fget=lambda self: 'hahhaah'),  # Todo: add another attr AA
    __getattribute__=g_getattribute,
    __setattr__=g_setattribute,
))

if __name__ == "__main__":
    main()
