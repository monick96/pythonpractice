import random

options = ('piedra', 'papel','tijera')
print('🥌 📋 ✂ ')

computer_wins = 0
user_wins = 0
rounds = 1

user_name = input('Ingrese su nombre => ')
user_name = user_name.capitalize()


while True:
  print('*' * 40)
  print('RONDA ', rounds)
  print('Computer Vs',user_name)
  print('Computer =>', computer_wins)
  print(user_name,'=>', user_wins)
  
  print('*' * 40)
 
  user_option = input('Piedra, Papel o Tijera=> ')
  user_option = user_option.lower()
  rounds+=1
  
  if not user_option in options:
    print(user_name,'Esa opcion no es valida')
    continue
    
  computer_option = random.choice(options)
  
  print(user_name,'elegiste=>', user_option)
  print('Computer eligio=>', computer_option)
  
  
  if user_option == computer_option:
    print('Empate!')
    
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a Tijera')
      print(user_name, 'gano!')
      user_wins+=1  
    else:
      print('Papel gana a Piedra')
      print('Computer gano!')
      computer_wins+=1
      
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a Piedra')
      print(user_name, 'gano!')
      user_wins+=1
    else:
      print(' Tijera gana a Papel')
      print('Computer gano!')
      computer_wins+=1
  
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Tijera gana a Papel')
      print(user_name, 'gano!')
      user_wins+=1
    else:
      print('Piedra gana a Tijera')
      print('Computer gano!')
      computer_wins+=1
  if user_wins==2:
    print(user_name,' la computadora ya no tiene oportunidad, ganaste 😺!')
    break
    
  if computer_wins == 2:
    print(user_name,'ya no tenes oportunidad contra la Computadora, perdiste 😿!')
    break
  