
def binary_search():
    li = [10,20,30,40,50,60,70]
    value = 70
    low = 0
    high = len(li)-1

    while low <= high:
        mid = (low+high)//2
        print(low,high,mid)
        if li[mid]==value:
            return 1
        if li[mid]>value:
            high = mid-1
        if li[mid]<value:
            low = mid+1
    return -1


def first_occurance():
    l = [5,10,10,20,20]
    value = 20
    low = 0
    high = len(l)-1

    while low <= high:
        mid = (low+high)//2
        if l[mid] < value:
            low = mid+1
        elif l[mid] > value:
            high = mid-1
        else:
            if mid == 0 or l[mid] == l[mid-1]:
                high = mid-1
            else:
                return mid


def last_occurance():
    l = [10,20,20,30,30,50]
    value = 50
    low = 0
    high = len(l)-1

    while low <= high:
        mid = (low+high)//2

        if l[mid] < value:
            low = mid+1
        elif l[mid]> value:
            high = mid-1
        else:
            if mid == len(l)-1 or l[mid] != l[mid+1]:
                return mid
            else:
                low = mid+1
    return -1

def count_occurances():
    l = [10,20,20,30,30,30,30,50]
    value = 30
    low = 0
    high = len(l)-1
    count = 0
    while low <= high:
        mid = (low+high)//2
        if l[mid] < value:
            low = mid+1
        elif l[mid]> value:
            high = mid-1

        else:
            count+=1
            if mid == 0 or mid == len(l)-1:
                return count  
            l.pop(mid)
            print(l,mid)

    if count:
        return count
    else:
        return -1

# print(count_occurances())


def find_ones():
    l = [0,0,0,0,1,1,1,1]
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low+high)//2
        print(mid)
        if l[mid] != 1:
            low = mid +1
        else:
            if l[mid] == l[mid-1]:
                high = mid-1
            else:
                return len(l) - mid
    return 0


def square_root():
    x = 25
    i = 1
    while i*i <= x:
        i+=1
    return (i-1)
