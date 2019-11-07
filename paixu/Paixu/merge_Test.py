def merge_sort(alist):
    if len(alist)==1:
        return alist
    mid=len(alist)//2
    left=alist[:mid]
    right=alist[mid:]
    l1=merge_sort(left)
    r2=merge_sort(right)
    return merge(l1,r2)

def merge(left,right):
    result=[]
    while len(left)>0 and len(right)>0:
        if left[0]<right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result=result+left
    result=result+right
    return result

if __name__=='__main__':
    print(merge_sort([6,5,4,3,2,1]))
