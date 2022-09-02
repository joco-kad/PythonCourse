from typing import List
from functools import reduce

from model.order import Order


class Customer:
	def __init__(self, name: str, city: str):
		self._name = name
		self._city = city
		self._orders = []

	def __str__(self) -> str:
		od = reduce(lambda acc, o: f'{acc}, {o}', self._orders)
		return f'{self.name} aus {self._city} hat geordert: {od}'

	@property
	def name(self) -> str:
		return self._name

	@property
	def city(self) -> str:
		return self._city

	@property
	def orders(self) -> List[Order]:
		return self._orders.copy()

	def has_orders(self) -> bool:
		return self.order_count > 0

	def add_order(self, order: Order) -> bool:
		return self._orders.append(order)
