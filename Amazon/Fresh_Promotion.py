def getPromotion(codeList, shoppingCart):
    sn = len(shoppingCart)
    i = 0

    while i < sn:
        tmp = i
        if len(codeList) == 0:
            return 1
        
        code = codeList[0]
        j = 0
        while i<sn and j < len(code) and (shoppingCart[i] == code[j] or code[j] == 'anything'):
            i += 1
            j += 1

        if j == len(code):
            codeList.pop(0)
        else:
            i = tmp + 1
        

    return 1 if len(codeList) == 0 else 0

codeList1 = [['apple', 'apple'], ['banana', 'anything', 'banana']] 
shoppingCart1 = ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']
codeList2 = [['apple', 'apple'], ['banana', 'anything', 'banana']]
shoppingCart2 = ['banana', 'orange', 'banana', 'apple', 'apple']
codeList3 = [['apple', 'apple'], ['banana', 'anything', 'banana']] 
shoppingCart3 = ['apple', 'banana', 'apple', 'banana', 'orange', 'banana']
codeList4 = [['apple', 'apple'], ['apple', 'apple', 'banana']] 
shoppingCart4 = ['apple', 'apple', 'apple', 'banana']
codeList5 =[['orange', 'banana', 'orange'], ['apple', 'apple']]
shoppingCart5 = ['orange', 'apple', 'apple', 'orange', 'banana', 'orange']
codeList6 = [['apple', 'apple'],['orange', 'banana', 'orange'],['pear', 'orange', 'grape']]
shoppingCart6 = ['orange', 'apple', 'apple', 'orange', 'banana', 'orange', 'pear', 'grape']
codeList7 = [['apple', 'apple'],['orange', 'anything', 'orange']]
shoppingCart7 = ['orange', 'apple', 'apple', 'orange', 'mango', 'orange']
codeList8 = [['apple', 'apple'],['orange', 'banana', 'orange']]
shoppingCart8 = ['orange', 'apple', 'apple', 'orange', 'apple', 'orange', 'banana', 'orange']

print(getPromotion(codeList8, shoppingCart8))