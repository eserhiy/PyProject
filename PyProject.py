a = 2.2
c = 'Hello'
b = int(4.8)
family = ['Anna','Victor','Alex']
print(a, b)
print( b)
print(f'Тип a: {type(a)}')
print(f'Тип b: {type(b)}')
print(f'Тип c: {type(c)}')
print(f'Тип family: {type(family)}') 
print('========================')
print(f'Тип family: {type(c)}')
print(f'ID a: {id(a)}') 

import keyword
kw_list = keyword.kwlist
print(kw_list)
for kw in kw_list:
    print(kw)
