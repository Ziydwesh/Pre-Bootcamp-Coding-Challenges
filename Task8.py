time = int(input("Enter number:"))

hours = int(time / 60)
minutes = (time * 60) % 60

print("%d hours, %02d minutes" % (hours, minutes))