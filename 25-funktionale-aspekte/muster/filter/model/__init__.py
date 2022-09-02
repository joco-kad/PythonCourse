import yaml as y

from model.customer import Customer
from model.product import Product
from model.order import Order

with open('model/data.yml') as f:
	data: dict = y.load(f, Loader=y.loader.SafeLoader)

_product_by_id = {}
_products_data = data['products']
for pd in _products_data:
	_product_by_id[pd['id']] = Product(pd['name'], pd['price'])

_order_by_id = {}
_orders_data = data['orders']
for od in _orders_data:
	products = []
	for p_id in od['products']:
		products.append(_product_by_id[p_id['id']])
	_order_by_id[od['id']] = Order(products)

_customers_data = data['customers']
customers = []
for cd in _customers_data:
	c = Customer(cd['name'], cd['city'])
	customers.append(c)
	for od in cd['orders']:
		c.add_order(_order_by_id[od['id']])

