from typing import List

from model.product import Product
from functools import reduce


class Order:
	def __init__(self, products: List[Product]):
		self._products = products

	def __str__(self) -> str:
		return reduce(lambda acc, p: f'{acc} {p}', self._products)