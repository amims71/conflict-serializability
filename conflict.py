from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):

        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour]:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if not visited[node]:
                if self.isCyclicUtil(node, visited, recStack):
                    return True
        return False


string = 'w3(A);r1(A);w1(B);r2(B);w2(C);r3(C)'

transactions = string.split(";")
# print(transactions)
septList = []
for transaction in transactions:
    # print(transaction)
    transaction = list(transaction)
    septList.append((transaction[0], transaction[1], transaction[3]))
    # print(septList)
# print(septList)

paths = []
g = Graph(4)
for i in range(len(septList)):
    for j in range(i + 1, len(septList)):
        # if j==i:continue
        if septList[i][1] == septList[j][1]: continue
        if septList[i][2] == septList[j][2]:
            if septList[i][0] == septList[j][0] == 'r': continue
            if (septList[i][1], septList[j][1]) in paths: continue
            paths.append((int(septList[i][1]), int(septList[j][1])))
            g.addEdge(int(septList[i][1]), int(septList[j][1]))
            # print(int(septList[i][1]), int(septList[j][1]))
print(paths)

if g.isCyclic() == 1:
    print("It has a cycle, so it is not conflict serializable.")
else:
    print("It has no cycle, so it is conflict serializable.")
