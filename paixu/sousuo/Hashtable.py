"""
散列表：使用+1线性探测法
hashfunction:散列值
rehash:寻找下一个槽
put(key,data)添加数据
get()获取数值
def __getitem__(self,key):可使用[]访问数值
def __setitem__(self,key,data):可使用[]添加数值
"""
class HashTable:
    def __init__(self):
        self.size=11
        self.slots=[None]*self.size
        self.data=[None]*self.size
    def hashfunction(self,key,size):
        return key%size
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    def put(self,key,data):
        hashvalue=self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        else:
            nextplots=self.rehash(hashvalue,len(self.slots))
            while self.slots[nextplots]!=None and \
                    self.slots[nextplots]!=key:
                nextplots=self.rehash(nextplots,len(self.slots))
            if self.slots[nextplots]==None:
                self.slots[nextplots]=key
                self.data[nextplots]=data
            else:
                self.data[nextplots]=data  #替换
    def get(self,key):
        startslot=self.hashfunction(key,len(self.slots))
        data=None
        stop=False
        found=False
        pos=startslot
        while self.slots[pos]!=None and not stop and not found:
            if self.slots[pos]==key:
                found=True
                data=self.data[pos]
            else:
                pos=self.rehash(pos,len(self.slots))
                if pos==startslot:
                    stop=True
            return data
    def __getitem__(self,key):
        return self.get(key)
    def __setitem__(self,key,data):
        return self.put(key,data)
if __name__=='__main__':
    H=HashTable()
    H[54]="cat"
    H[26]='dog'
    print(H.data)
