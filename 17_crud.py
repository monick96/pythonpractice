#CRUD Create, Read, Update & Delete
'''
append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
'''

numbers = [1,2,3,4,5,6]
print(numbers[1])
numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0,'hi')
print(numbers)

numbers.insert(3,'change')
print(numbers)

tasks = ['todo 1','todo 2','todo 3','todo 4']
new_list = numbers + tasks
print(new_list)
index = new_list.index('todo 2')
print(new_list[index])
new_list[index] = 'todo change'
print(new_list[index])
print(new_list)
new_list.remove('todo 1')
print(new_list)
new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

numbers_a = [1,10,4,56,20]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'mi','fa']
strings.sort()
print(strings)

#no se puede ordenar una lista con distintos tipos de datos

