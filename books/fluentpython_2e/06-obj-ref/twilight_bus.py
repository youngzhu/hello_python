"""
>>> basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
>>> bus = TwilightBus(basketball_team)
>>> bus.drop('Tina')
>>> bus.drop('Pat')
>>> basketball_team
['Sue', 'Maya', 'Diana']
"""

# tag::TWILIGHT_BUS_CLASS[]
class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  # 如果传参为 None，则创建一个新的空列表
        else:
            # self.passengers = passengers  # 问题：下车后，篮球队的成员会消失
            self.passengers = list(passengers) # 创建副本，解决问题

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)  # <3>
# end::TWILIGHT_BUS_CLASS[]

