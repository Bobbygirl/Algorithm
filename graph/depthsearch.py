"""
深度优先搜索和宽度优先搜索
"""
from collections import deque

class graph(object):
    """
    定义一个图类
    """

    def __init__(self):
        """
        初始化

        """
        #order，存储节点
        self.order=[]
        #存储邻居节点，
        self.neighbors={}
    def add_node(self,node):
        """
        添加节点

        """
        key,value=node
        #实现key与val的对应。即跟节点和孩子节点的连接
        self.neighbors[key]=value


    def BFS(self,root):
        """
        宽度优先搜索
        """

        if root != None:
            """
            判断节点是否为空
            """
            #初始化队列
            qeue = deque()
            #添加跟节点
            qeue.append(root)
        else:
            return -1

        while qeue:
            """
            遍历队列
            """
            #删除节点
            person=qeue.popleft()
            #在order中添加节点
            self.order.append(person)

            if (person in self.neighbors.keys()):
                """
                判断当前节点是否neigbors中的key值
                """
                #self.neighbors[person]返回的是集合
                qeue +=self.neighbors[person]

    def DFS(self,root):
        """

        深度优先搜索
        """
        if root!=None:
            qeue=deque()
            qeue.append(root)
        else:
            return -1
        while qeue:
            person=qeue.popleft()
            self.order.append(person)

            if (person in self.neighbors.keys()):
                #获取key的集合
               temp=self.neighbors[person]
                #将集合反转
               temp.reverse()

               for tem in temp:
                   #反转后进行遍历添加到队列中
                   qeue.appendleft(tem)
    def node_print(self):
        for index in self.order:
            print(index, end='  ')



if __name__ == '__main__':
    # 创建一个二叉树图
    g = graph()
    g.add_node(('A', ['B', 'C']))
    g.add_node(('B', ['D', 'E']))
    g.add_node(('C', ['F']))

    # 进行宽度优先搜索
    g.BFS('A')
    print('宽度优先搜索:')
    print('  ', end='  ')
    g.node_print()
   

    # 进行深度优先搜索
    print('\n\n深度优先搜索:')
    print('  ', end='  ')
    g.DFS('A')
    g.node_print()
    print()




