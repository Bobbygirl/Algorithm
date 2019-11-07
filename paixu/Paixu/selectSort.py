"""
选择排序
每一次遍历都会找到最大项
"""
def selectSort(alist):
    for num in range(len(alist)-1,0,-1):
        Max=0
        for i in range(1,num+1):

            if alist[i]>alist[Max]:
                Max=i
        temp=alist[num]
        alist[num]=alist[Max]
        alist[Max]=temp
    return alist

if __name__=="__main__":
    print(selectSort([26,54,93,17,77,31,44,55,20]))