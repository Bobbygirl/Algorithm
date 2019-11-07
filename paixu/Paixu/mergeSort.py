"""
归并排序
"""
def mergeSort(alist):
    if len(alist)==1:
        return alist
    mid=len(alist)//2
    left=alist[:mid]
    right=alist[mid:]
    l1=mergeSort(left)
    r1=mergeSort(right)
    return merge_sort(l1,r1)

def merge_sort(left,right):
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
    print(mergeSort([6,5,4,3,2,1]))