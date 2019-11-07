"""
希尔排序：是插入排序的改进
"""
# def shellSort(alist):
#     sublistcount=len(alist)//2
#     while sublistcount>0:
#         for startpos in range(sublistcount):
#             gapInsertionSort(alist,startpos,sublistcount)
#         sublistcount=sublistcount//2
#     return alist
#
#
# def gapInsertionSort(alist,start,gap):
#     for i in range(start+gap,len(alist),gap):
#         current=alist[i]
#         pos=i
#         while pos>=gap and alist[pos-gap]>current:
#             alist[pos]=alist[pos-gap]
#             pos=pos-gap
#             alist[pos]=current
def shellSort(alist):
    n=len(alist)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=alist[i]
            j=i
            while j>=gap and alist[j-gap]>temp:
                alist[j]=alist[j-gap]
                j=j-gap
                alist[j]=temp
        gap=gap//2
    return alist



if __name__=='__main__':
    print(shellSort([54,26,93,17,77,31,44,55,20]))