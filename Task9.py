numbers = [3, 5]
maximum = 1000

 sum = 0
for i in range(0, maximum):
    if i%3 == 0 or i%5 == 0:
       sum += i


print(sum)
