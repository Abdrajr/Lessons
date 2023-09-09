CatNames = []
while True:
    print('Enter name of a cat'  + str(len(CatNames) + 1) + ' (or enter nothing to stop. ): ')
    name = input()
    if name == '':
        break
    CatNames = CatNames + [name] 
print('the cat names are: ')
for name in CatNames:
    print('' + name )