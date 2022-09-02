class Product:
	def __init__(self, name, price):
		self._name = name
		self._price = price

	def __str__(self) -> str:
		return f'{self.name} Preis: {self.price}'

	@property
	def name(self) -> str:
		return self._name

	@property
	def price(self) -> float:
		return self._price
