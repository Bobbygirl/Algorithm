from pythonds.graphs import Graph
class Vertex:
    """
    描述图表中顶点的信息
    """
    def __init__(self,key):
        self.id=key
        self.connectionTo={}
    def addNeighbors(self,nbr,weight=0):
        self.connectionTo[nbr]=weight
    def  __str__(self):
        return str(self.id)+'connectionTo：'+str([x.id for x in self.connectionTo])

    def getConnections(self):
        return self.connectionTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectionTo[nbr]


class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0
    def addVertex(self,key):
        self.numVertices +=1
        newVertex=Vertex(key)
        self.vertList[key]=newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self,n):
        return n in self.vertList
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv=self.addVertex(f)
        if t not in self.vertList:
            nv=self.addVertex(t)
        self.vertList[f].addNeighbors(self.vertList[t],cost)
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())


if __name__=='__main__':
    g =Graph()
    for i in range(6):
        g.addVertex(i)
    print(g.vertList)
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    for v in g :
        for w in v.getConnections():
            # print("(%s,%s)"% (v.getId(),w.getId()))
            print("({},{})".format(v.getId(),w.getId()))