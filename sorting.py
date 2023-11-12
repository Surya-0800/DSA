# Bubble Sort
def bubble_sort():
    lis = [1,4,3,7,3,6577,234,768,123]
    l = len(lis)
    for i in range(l):
        for j in range(l-i-1):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1]= lis[j+1],lis[j]

    return lis

def insertion_sort():
    lis = [1,4,3,7,3,6577,234,768,123]
    l = len(lis)

    for i in range(l):
        anc = i
        while anc >0:
            if lis[i]<lis[anc]:
                print(lis)
                lis[i],lis[anc] = lis[anc],lis[i]
        anc -= 1
    return lis


# print(insertion_sort())
# print(insertion_sort())


def merge_sorted_arrays():
    a  = [10,15]
    b = [5,6,6,30,40]
    res = []
    al = len(a)
    bl = len(b)
    ai = 0
    bi = 0

    while ai < al and bi <bl:
        if a[ai] < b[bi]:
            res.append(a[ai])
            ai +=1
        else:
            res.append(b[bi])
            bi+=1

    while ai < al:
        res.append(a[ai])
        ai+=1
    while bi < bl:
        res.append(b[bi])
        bi+=1

    return res
print(merge_sorted_arrays())