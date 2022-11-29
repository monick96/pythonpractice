#JS - Python
#Arreglo - Lista
#Objeto - Diccionario
#Los diccionarios se compones de llave, valor.
# muy similares a un archivo .json
'''
DICICIONARIOS, TUPLAS Y LISTAS
*LISTA --> lista = [ ];

*TUPLAS --> tupla = ( );

DICCIONARIO —> diccionario = { }
'''

my_dict = {}
print(type(my_dict))

my_dict = {
  'avion': "bla bla bla",
  'name': 'Nicolas',
  'last_name': 'Molina',
  'age': 90
}

print(my_dict)
print(len(my_dict))
print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('la'))  #si no se encuantra en el dicionario arroja 'None'
#print(my_dict['la']) da error
print('avion' in my_dict)
print('la' in my_dict)
