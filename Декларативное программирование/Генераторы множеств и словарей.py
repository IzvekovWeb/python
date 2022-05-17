def number_of_unique_letters(x):
    return len({char.lower() for char in x if char.isalpha()})

print(number_of_unique_letters("") ) # 0
print(number_of_unique_letters("abc") ) # 3
print(number_of_unique_letters("A-a-a-a-a-a!") ) # 1
print(number_of_unique_letters("\\(O_o)/"))  # 1
print(number_of_unique_letters("AaBbCcDd") ) # 4
