"""
希尔排序
"""
def shellsort(alist):
    gap=len(alist)//2
    while gap>0:
        for i in range(gap,len(alist)):
            j=i
            temp = alist[i]
            if j>=gap and alist[j]<alist[j-gap]:
                alist[j]=alist[j-gap]
                j=j-gap
                alist[j]=temp
        gap=gap//2
    return alist




if __name__=='__main__':
    print(shellsort([54,26,93,17,77,31,44,55,20]))