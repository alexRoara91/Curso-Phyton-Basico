# own modules
# third party modules 
# python modules

# Módulos preconstruidos
from datetime import timedelta, date

# import fmath
from fmath import add, substract

from colorama import Fore, Style, init
init(convert = True)


print(date.today())

add(3,3)

substract(3,1)



print(Fore.RED + "Hello world")
print(Fore.YELLOW + "Hello world")
print(Fore.BLUE + "Hello world")
print(Fore.GREEN + "Hello world")