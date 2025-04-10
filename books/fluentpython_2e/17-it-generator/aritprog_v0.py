"""
Arithmetic progression class

    >>> ap = ArithmeticProgression(1, .5, 3)
    >>> list(ap)
    [1.0, 1.5, 2.0, 2.5]


"""


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> "infinite" series

    def __iter__(self):
        # 获取 self.begin 与 self.step 之和的类型。
        # 例如，如果一个是 int 类型，另一个是 float 类型，那么 result_type 是 float类型
        result_type = type(self.begin + self.step)
        # 把 self.begin 赋值给 result，不过先强制转换成前面的加法算式得到的类型
        result = result_type(self.begin)
        forever = self.end is None
        while forever or result < self.end:
            yield result
            result += self.step
