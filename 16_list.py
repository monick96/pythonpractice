#list o array

nums = [1,2,3,4]
print(nums)
print(type(nums))

tasks = ['make a dishes','cook','cleaner']
print(tasks)
types = [0,False,'hi']
print(types)

print(nums[0])
print(tasks[1])

#mutacion

text = 'hola' #strings son inmutables
#text[0] = 'w' is not posible, we need use replace

tasks[0] = "watch platzi courses"
print(tasks)
tasks[0] = "do the disdhes"
print(tasks)
print(nums[:3])
print(True in types)
print('hi' in types)