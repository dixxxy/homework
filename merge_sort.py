#合并两个有序列表

#递归
def _recursion_merge_sort2(l1,l2,tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1,l2,tmp)
def recursion_merge_sort2(l1,l2):
    return _recursion_merge_sort2(l1,l2,[])

l1 = [1,3,5,7,9]
l2 = [2,4,6,8,9]

print(recursion_merge_sort2(l1,l2))

#循环
def loop_merge_sort(l1,l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    tmp.extend(l1)
    tmp.extend(l2)
    return tmp
