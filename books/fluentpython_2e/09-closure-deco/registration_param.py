# tag::REGISTRATION_PARAM[]

registry = set()  # registry 现在是一个 set 对象，这样添加和删除函数的速度更快

def register(active=True):  # <2>
    def decorate(func):  # <3>
        print('running register'
              f'(active={active})->decorate({func})')
        if active:   # <4>
            registry.add(func)
        else:
            registry.discard(func)  # <5>

        return func  # <6>
    return decorate  # <7>

@register(active=False)  # <8>
def f1():
    print('running f1()')

@register()  # 即使不传入参数，register 也必须作为函数调用
def f2():
    print('running f2()')

def f3():
    print('running f3()')

# end::REGISTRATION_PARAM[]
