from typing import List

from model import customers, Customer


def sort_orders(reverse: bool) -> List[Customer]:
    return sorted(customers, key=lambda _c: _c.order_count, reverse=reverse)


if __name__ == '__main__':
    print('Absteigend')
    for c in sort_orders(True):
        print(c)
    print('Aufsteigend')
    for c in sort_orders(False):
        print(c)

