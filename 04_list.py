demolist = ["list",True,34,3.56,[3,3,1]]
colors = ['red','green','blue']

numbers_list = list((1,2,3,4))
print (type(numbers_list))

r = list(range(1,1000))
print(r)

print(len(demolist))
print(colors[-2]) #<-- indice negativo

print(dir(colors))

# con append agregamos un elemento
colors.append('violet')
colors.extend(['purple','orange'])
print(colors)

# colors.extend('pink','black')

# con insert es posible usar índices negativos
colors.insert(-1,'silver')

colors.sort(reverse=True)
colors.append('red')
print('----------------')
print(colors.count('red'))





