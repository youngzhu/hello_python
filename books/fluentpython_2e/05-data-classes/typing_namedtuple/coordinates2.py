"""
``Coordinate``: a simple ``NamedTuple`` subclass

This version has a field with a default value::

    >>> moscow = Coordinate(55.756, 37.617)
    >>> moscow
    Coordinate(lat=55.756, lon=37.617, reference='WGS84')

"""

# tag::COORDINATE[]
from typing import NamedTuple

class Coordinate(NamedTuple):
    # 更像是一种文档说明
    # 因为Python不检查类型
    lat: float                # 指定类型
    lon: float
    reference: str = 'WGS84'  # 指定类型+默认值
# end::COORDINATE[]
