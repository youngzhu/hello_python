from typing import Protocol, runtime_checkable
from randompick import RandomPicker

@runtime_checkable  # <1>
class LoadableRandomPicker(RandomPicker, Protocol):  # 每个协议都必须明确把 typing.Protocol 列出来，作为基类。另外，再列出要扩展的协议。这与 Python 中的继承不是一回事
    def load(self, Iterable) -> None: ...  # <3>
