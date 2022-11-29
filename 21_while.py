'''
Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición (es decir, mientras la condición tenga el valor True).

El bucle while evalúa una condición y luego ejecuta un bloque de código si la condición es verdadera. El bloque de código se ejecuta repetidamente hasta que la condición llega ser o es falsa
'''

'''
if True:
  print('se ejecuto')

counter= 0
while counter<10:
  counter +=1
  print(counter)
'''
'''
counter=0
while counter<20:
  counter +=1
  if counter == 15:
    break
  print(counter)
'''


counter=0
while counter<20:
  counter +=1
  if counter <15:
    continue
  print(counter)

  