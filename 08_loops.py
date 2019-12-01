import random
import time
# ------------------------------------
numbers = []

for x in range(0,20):
    numbers.append(x)
    if ((x%2) == 0):
        print('WWWWWWWWWWWWWWWWWWW')
    else:
        print('nnnnnnnnnnnnnnnnnnn')
print('')
print('***********************  ')
print('')
for y in numbers:
    if ((y%2) == 0):
        print('llllllllllllllllllll')
    else:
        print('IIIIIIIIIIIIIIIIIIII')


esp = ' ' 

for z in range(0,10):
    for y in numbers:
        if ((y%2) == 0):
            print('lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll')
        else:
            print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')

row = ''



#while True:
 #  print('caca')
 #  time.sleep(1)





for w in range(0,90):
    for v in range(0,90):
        
        digit = str(random.randrange(0,2,1))
        row = row + digit
        

    print(row)
    time.sleep(0.100)