text = 'She knows how to program in Python'

'''
print('Javascript' in text)
print('Python' in text)

if 'Python' in text:
  print('You chose well!')
else:
  print('You chose well too!')

size = len('love')
print(size)
'''
#len
size = len(text)
print(size, '\n')

print(text, '\n')
#upper
print(text.upper(), '\n')
print(text.lower(), '\n')

#count
print(text.count('e'))

#swapcase
print(text.swapcase())
#startswith
print(text.startswith('She'))
#endswith
print(text.endswith('Go'))
#replace
print(text.replace('Python','Go'))

text_2 = 'this is a title'
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print('569'.isdigit())
