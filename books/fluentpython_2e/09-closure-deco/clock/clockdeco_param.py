# clockdeco_param.py

"""
>>> snooze(.1)  # doctest: +ELLIPSIS
[0.101...s] snooze(0.1) -> None
>>> clock('{name}: {elapsed}')(time.sleep)(.2)  # doctest: +ELLIPSIS
sleep: 0.20...
>>> clock('{name}({args}) dt={elapsed:0.3f}s')(time.sleep)(.2)
sleep(0.2) dt=0.201s
"""

# tag::CLOCKDECO_PARAM[]
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):  # <1>
    def decorate(func):      # <2>
        def clocked(*_args): # <3>
            t0 = time.perf_counter()
            _result = func(*_args)  # <4>
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)  # <5>
            result = repr(_result)  # <6>
            print(fmt.format(**locals()))  # 这里使用 **locals() 是为了在 fmt 中引用 clocked 的局部变量
            return _result  # <8>
        return clocked  # <9>
    return decorate  # <10>

if __name__ == '__main__':

    @clock()  # <11>
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)

# end::CLOCKDECO_PARAM[]
