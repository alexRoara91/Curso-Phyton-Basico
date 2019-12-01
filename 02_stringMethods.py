myStr = "Hello World"

# dir() = obtenemos las funciones qe podemos obtener con strings
# print(dir(myStr))

print("\n [string].upper(): " + myStr.upper())
print("\n [string].lower(): " + myStr.lower())
print("\n [string].swapcase(): " + myStr.swapcase())
print("\n [string].capitalize(): " + myStr.capitalize())
print("\n [string].replace(): " + myStr.replace("World","Welt"))

print("[a string].count(' '): ")
print(myStr.count(' '))

print("\n [a string].startswith(' '): ")
print(myStr.startswith('He'))

print("\n [a string].endswith(' '): ")
print(myStr.endswith('World'))

print(myStr.split(' '))
print(myStr.find('z'))

#The len() function returns the number of items (length) in an object.
print(len(myStr))
print(myStr.index('H'))

print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[0])
print(myStr[1])
print(myStr[2])
print(myStr[3])
print(myStr[4])
print(myStr[5])
print(myStr[6])
print(myStr[7])
print(myStr[8])
print(myStr[9])
print(myStr[10])
print(myStr[-5])

print("Concatenamos la frase con '+': " + myStr)

print(format(myStr))








