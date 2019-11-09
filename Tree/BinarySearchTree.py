"""
二叉搜索树(未完成)
"""
class BinarySearchTree:
    """
    二叉搜索树
    """
    def __init__(self):
        self.root=None
        self.size=0
    def lengh(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root=TreeNode(key,val)
        self.size+=1
    def _put(self,key,val,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.hasLeftChild)
            else:
                currentNode.leftChild=TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                if currentNode.hasRightChild():
                    self._put(key, val, currentNode.rightChild)
                else:
                    currentNode.rightChild = TreeNode(key, val, parent=currentNode)
    def __setitem__(self,k,v):
        self.put(k,v)
    def delete(self,key):
        if self.size>1:
            noderemove=self._get(key,self.root)
            if noderemove:
                self.delete(noderemove)
                self.size-=1
            else:
                return KeyError('error,key not in tree')
        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size-=1
        else:
            return KeyError('error,key not in tree')

    def __delitem__(self,key):
        self.delete(key)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key==key:
            return currentNode
        elif key<currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
    def __getitem__(self,key):
        res=self.get(key)
        if res:
            return res
        else:
            raise KeyError('the key not in tree')
    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


if __name__=='__main__':
    mytree=BinarySearchTree()
    mytree[3]='red'
    mytree[4]='blue'
    mytree[6]='yellow'
    mytree[2]='at'
    print(mytree[4])

