def addToInventary(inventary, addedItems):
    for i in range(len(addedItems)):

        if addedItems[i] not in inventary:
            inventary[addedItems[i]] = 1
        else:
            inventary[addedItems[i]] = inventary[addedItems[i]] + 1

    return inventary

def displayInventary(base): # 
    print('Inventary:')
    itemTotal = 0
    for k, v in base.items():
        print(str(v) + ' ' + k)
        itemTotal += v
    print('Total number of items: ' + str(itemTotal))
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoop = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventary(inv, dragonLoop)
displayInventary(inv)
