from random import randrange

from tombola import Tombola

@Tombola.register  # 把 Tombolist 注册为 Tombola 的虚拟子类
class TomboList(list):  # <2>

    def pick(self):
        if self:  # <3>
            position = randrange(len(self))
            return self.pop(position)  # <4>
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend  # Tombolist.load 等同于 list.extend

    def loaded(self):
        return bool(self)  # <6>

    def inspect(self):
        return tuple(self)

# 始终可以这样调用 register。如果需要注册不是自己维护的类，却能满足指定的接口，就可以这么做
# Tombola.register(TomboList)  # <7>
