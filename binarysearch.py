def binarysearch(l,item):
    first = 0
    last = len(l)-1
    midpoint = (first + last) // 2
    found = False
    if l[midpoint] == item and not found:
        found = True
        return found
        print("%s是第%s个数字" % (item,midpoint+1))
    else:
        if l[midpoint] < item:
            first = midpoint + 1
            return found
        else:
            last = midpoint - 1
            return found
    print("%s是第%s个数字" % (item, midpoint + 1))


l = [1,2,3,5,8,10]
print(binarysearch(l,8))

