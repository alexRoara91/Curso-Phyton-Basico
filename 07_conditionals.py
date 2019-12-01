x = int(input('insert your number'))
if x < 30:
    print('x is less than 30') 
elif x == 30:
    print('x is 30')
else:
    print('x is greater than 30')

print('**************************')
print('')
age = int(input('insert your age: '))

if age > 10 and age < 31:
    print('You are young')
else:
    print('you are not young')

if not(age > 64):
    print('You are not an old man')
else:
    print('you are an old man')