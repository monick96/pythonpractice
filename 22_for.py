'''
el for lo usamos cuando tenemos un numero de itereciones definidas
for el in range(20):
  print(el)

  for el in range(1,21):
  print(el)
'''
my_list = [25, 35, 60, 96, 63, 45]

for el in my_list:
  print(el)

my_tuple=(60, 40, 55, 64, 'nati', 'nico')

for e in my_tuple:
  print(e)

product = {
  'name': 'shirt',
  'price': 100,
  'stock': 89
}
for el in product:
   print(el)

#una forma
for key in product:
   print(key, '=>' ,product[key])

#otra forma
for key, value in product.items():
  print(key, '=>' , value)


people = [{
  'name': 'zule',
  'age': 34
},
{
  'name': 'nico',
  'age': 45
},
{
  'name':'sonic',
  'age': 25
}
]

for person in people:
  print(person)

for person in people:
  print('name =>', person['name'], '-','age => ', person['age'])