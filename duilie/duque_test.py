from 算法.队列.Deque import Deque
def palchecker(aString):
    dd=Deque()
    for ch in aString:
        dd.addRear(ch)
    flag=True
    while dd.size()>1:
        first=dd.removeFront()
        last=dd.removeRear()
        if first!=last:
            flag=False
    return flag

if __name__=='__main__':
   print(palchecker('abcdcba'))