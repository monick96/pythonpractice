name = 'Monica'
last_name = 'Melgarejo Esquivel'
age = 26
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Monica"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

#format
template = "Hello, my name is " + name + " and my last name is " + last_name
print('v1', template)

template = "Hello, my name is {} and my last name is {}".format(name, last_name)
print('v2', template)

template = f"Hello my name is {name} and my last name is {last_name}"
print('v3',template)

template = f"hello my name is {name} {last_name} and my age is {age}"
print('v4', template)

