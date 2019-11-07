"""
选择排序
原理：每次遍历选出最大的那个数字先记录下来然后通过比较放到数组最后
"""
def selectSort(alist):
    for i in range(len(alist)-1,0,-1):
        Max = 0
        for j in range(1,i+1):
            if alist[j]>alist[Max]:
                Max=j
        temp=alist[i]
        alist[i]=alist[Max]
        alist[Max]=temp
    return alist

if __name__=='__main__':
    print(selectSort([26,54,93,17,77,31,44,55,20]))