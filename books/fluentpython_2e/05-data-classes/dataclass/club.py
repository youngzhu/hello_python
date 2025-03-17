from dataclasses import dataclass, field

@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)
    # 把默认值设为 False，而且不提供给 __repr__ 方法使用
    athlete: bool = field(default=False, repr=False)

