x = 3.3
y = 1.1 + 2.2

print(x)
print(y)
print(x == y)

#comparar flotantes con round
print(x== round(y,1))

#comparar flotantes convirtiendo en string
y_str = format(y, ".2g")
print('str =>', y_str)
print(y_str == str(x))

#comparar con conversion matematica
print('*' * 10)

print(x, y)

tolerance = 0.00001

print(abs(x -y))
print(abs(x -y) < tolerance)









