#有序表的二分搜索
def binarySearch(alist,item):
    start=0
    end=len(alist)-1
    found=False
    while start<=end and not found:
        mid=(start+end)//2
        if alist[mid]==item:
            found=True
        else:
           if alist[mid]>item:
               end=mid-1
           else:
               start=mid+1
    return found

if __name__=='__main__':
    testlist=[2,4,5,6,7,8,9,10]
    print(binarySearch(testlist,10))