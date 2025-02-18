"""
metro_lat_long.py

Demonstration of nested tuple unpacking::

    >>> main()
                    |  latitude | longitude
    Mexico City     |   19.4333 |  -99.1333
    New York-Newark |   40.8086 |  -74.0204
    São Paulo       |  -23.5478 |  -46.6358

"""

# tag::MAIN[]
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        # 这个 match 的匹配对象是 record，即 metro_areas 中的各个元组
        match record:  # <1>
            # 一个 case 子句由两部分组成：一部分是模式，另一部分是使用 if关键字指定的卫语句（guard clause，可选）
            case [name, _, _, (lat, lon)] if lon <= 0:  # <2>
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
# end::MAIN[]

if __name__ == '__main__':
    main()
