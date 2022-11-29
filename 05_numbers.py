lives = 3
print(type(lives))
age = 12
budget = 100

temperature = 12.12

print(type(temperature))

lives = 2
print(lives)
lives = 1
print(lives)

lives = 12 + 15
print(lives)

lives += 1
print(lives)

lives = lives - 1
print(lives)

lives -= 1
print(lives)

#num muy grandes o pequeños los representa con notacion cientifica
num = 4500000000000000000000000000000000.1
print(num)

num2 = 0.00000000000000000000000001
print(num2)

#calcular presupesto  promedio de 3 meses
'''
budget_ene = 300
budget_feb = 400
budget_mar = 500
'''
budget_ene = int(input('What is your budget for January?  '))
budget_feb = int(input('What is your budget for February? '))
budget_mar = int(input('What is your budget for March? '))

ave = (budget_ene + budget_feb + budget_mar) / 3

print('January Budget=> ', budget_ene)
print('February Budget=> ', budget_feb)
print('March Budget=> ', budget_mar)
print('The average budget for January, February and March was: ', ave)
