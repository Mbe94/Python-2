items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

prices = list(map(lambda item: item['price'], items))
print(items)
print(prices)

def add_taxes(item):
  new_items = item.copy()
  new_items['taxes'] = new_items['price'] * .19
  return new_items

new_items = list(map(add_taxes, items))
print('New List')
print(new_items)
print('Old List')
print(items)