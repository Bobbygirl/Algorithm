"""
树的定义
通过嵌套列表实现树
"""
def BinaryTree(r):
    return[r,[],[]]

def insertleft(root,newBranch):
    t=root.pop(1)
    if len(t)>1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root
def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch,[],t])
    else:
        root.insert(2, [newBranch, [],[]])
    return root
def getRootVal(root):
    return root[0]
def setRootVal(root,newVal):
    root[0]=newVal
def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]


if __name__=='__main__':
    r=BinaryTree(3)
    insertleft(r,4)
    insertleft(r,5)
    insertRight(r,6)
    insertRight(r,7)
    l=getLeftChild(r)
    # print(l)
    # setRootVal(l,9)
    # print(r)
    # insertleft(l,11)
    # print(l)
    print(r)
