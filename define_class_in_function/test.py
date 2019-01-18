class A:
    def foo(self):
        return 123


class_defined = None

def wrapper(func):
    def f(*args, **kwargs):
        ret = foo(*args, **kwargs)
        if not class_defined:
            class B:
                def bar(self):
                    return 234
        return ret
    return f

a = A()
foo = wrapper(a.foo)

b = B()
print(b.bar())
