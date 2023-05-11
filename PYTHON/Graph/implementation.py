class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, val):
        self.adjacentList[val] = []
        self.numberOfNodes += 1

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnection(self, gr):
        for item in gr:
            print(f"{item} ==>", end=" ")
            for i in gr[item]:
                print(i, end=" ")
            print("\n")

myGraph = Graph()
myGraph.addVertex("0")
myGraph.addVertex("1")
myGraph.addVertex("2")
myGraph.addVertex("3")
myGraph.addVertex("4")
myGraph.addVertex("5")
myGraph.addVertex("6")

myGraph.addEdge("3", '1')
myGraph.addEdge("3", '4')
myGraph.addEdge("4", '2')
myGraph.addEdge("4", '5')
myGraph.addEdge("1", '2')
myGraph.addEdge("1", '0')
myGraph.addEdge("0", '2')
myGraph.addEdge("6", '5')

myGraph.showConnection(myGraph.adjacentList)

