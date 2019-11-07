"""
插入排序：总保持一个位置靠前的已排好序的子表
"""
def insertSort(alist):
    for i in range(1,len(alist)):
        j=i-1
        key=alist[i]
        while j>=0:
            if alist[j]>key:
                alist[j+1]=alist[j]
                alist[j]=key
            j=j-1
    return alist

if __name__=='__main__':
    print(insertSort([54,26,93,17,77,31,44,55,20]))