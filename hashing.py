def sumExists(arr, n, sums):
    i,j = 0,0
    while i < n :
        sumv = arr[i]+arr[j]
        if sumv==sums and i != j:
            return {arr[i],arr[j]}
        else:
            if j == (n-1):
                j = 0
                i +=1
            else:
                j+=1
    
    return 0



def linearProbing(hashSize, arr, sizeOfArray):
    arr2 = []
    for i in range(hashSize):
        arr2.append(-1)

    for index in range(sizeOfArray):
        if index < hashSize:
            i = arr[index]
        else:
            break
        
        ind = i%hashSize
        
        if arr2[ind] == -1:
            arr2.insert(ind,i)
            arr2.pop(ind+1)
        else:
            print(ind)
            if ind == (hashSize-1):
                x = 0
            else:
                x = ind+1
            while x != ind:
                if arr2[x]==-1:
                    arr2.insert(x,i)
                    arr2.pop(x+1)
                    break
                elif x == hashSize-1:
                    x=0
                else:  
                    x+=1
    return arr2
                

hashSize = 19
sizeOfArray = 23 
arr = [944101,432332, 4730, 779357, 767178, 118088, 453314, 459419, 396271, 213804, 219101, 515641, 633968, 252800, 562126, 935684, 662662, 770828, 801862, 630757, 17307, 796521, 933071]
# print(linearProbing(hashSize, arr, sizeOfArray))


def countNonRepeated(arr,n):
    arr2 = []
    i = 0
    j = i+1
    tag = True
    while i < n-1:
        if arr[i] == arr[j]:
            i = i+1
            j = i+1
            tag = False
        else:
            j+=1
        if j >n-2:
            if tag:
                arr2.append(arr[i])
            i += 1
            j = i+1
            tag = True
        
    return arr2
print(countNonRepeated([1,1,2,2,3,3,4,5,6,7],10))
