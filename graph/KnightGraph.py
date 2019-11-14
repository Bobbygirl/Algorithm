"""
建立骑士周游图
"""
from pythonds.graphs import Graph
def KnightGraph(bdSize):
    ktGraph=Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeID=posToNodeId(row,col,bdSize)
            newpositions=genLegalMoves(row,col,bdSize)
            for e in newpositions:
                nid=posToNodeId(e[0],e[1],bdSize)
                ktGraph .addEdge(nodeID,nid)
    return ktGraph

def posToNodeId(row,column,board_size):
    return (row*board_size)+column

def genLegalMoves(x,y,bdSize):
    newMoves=[]
    moveOffsets=[(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(2,-1),(2,1)]
    for i in moveOffsets:
        newX=x+i[0]
        newY=y+i[1]
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX ,newY))
    return newMoves

def legalCoord(x,bdSize):
    if x>=0 and x<bdSize:
        return True
    else:
        return False
