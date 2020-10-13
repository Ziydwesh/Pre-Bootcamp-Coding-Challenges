x = float(input('Enter number:'))
y = float(input('Enter number:'))
z = float(input('Enter number:'))

if (x >= y) and (x >= z):
    maximum = x

elif (y >= x) and (y >= z):
    maximum = y

else:
    maximum = z

print("Maximum number is", maximum)
