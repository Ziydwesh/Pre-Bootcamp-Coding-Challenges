word1 = input("Enter first word:")
word2 = input("Enter second word:")

a = list(set(word1) & set(word2))

print("Common characters:")

for i in a:
     print(i)
