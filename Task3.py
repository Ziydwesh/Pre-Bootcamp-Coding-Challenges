def test_65(a, b):
    if a == 65 or b == 65 or (a + b) == 65:
        return True
    else:
       return False

print(test_65(65, 48))
print(test_65(39, 65))
print(test_65(38, 27))
print(test_65(13, 11))
