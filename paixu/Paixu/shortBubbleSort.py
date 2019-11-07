"""
短路冒泡排序：
可以发现列表已经排好时就立刻结束。
"""
def shortBubbleSort(alist):
    exchange=True
    passnum=len(alist)-1
    while passnum>0:
        exchange=False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchange=True
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
            passnum=passnum-1
    return alist

if __name__=='__main__':
    print(shortBubbleSort([12,14,16,11,18]))

