print('Available options \n')
print('1) KW => PK')
print('2) PK => KWH')

optionSelected = int(input('> '))

if optionSelected == 1:
    kw = float(input('KW: '))
    result = kw * 1.362
elif optionSelected == 2:
    pk = float(input('PK: '))
    result = pk * 0.7342143906020557
else :
    exit()

print(result)