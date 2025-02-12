import collections

# 用 collections.namedtuple 构建了一个简单的类，表示单张纸牌。
# 使用 namedtuple 构建只有属性而没有自定义方法的类对象，例如数据库中的一条记录
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
