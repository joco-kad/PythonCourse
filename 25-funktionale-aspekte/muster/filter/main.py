from typing import List

from model import customers, Customer


def filter_orders() -> List[Customer]:
    return list(filter(lambda c: c.has_orders, customers))


if __name__ == '__main__':
    for c in filter_orders():
        print(c)

