def test_3(a, b):
    if a == 3 or b == 3 & (a + b) ==3:
        return True
    else:
        return False

print(test_3(3, 5))
print(test_3(7, 3))
print(test_3(2, 1))
print(test_3(8, 5))
