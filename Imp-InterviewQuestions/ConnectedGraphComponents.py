# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
#
# Number of Connected Components in an Undirected Graph
#
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
#
# Return the number of connected components in the graph.
#
# example1:
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

# Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
# Output: 1
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        components = 0
        adjList = [[]] * n
        visited = [0] * n
        for i in range(n):
            adjList[i] = []
        for i in range(len(edges)):
            adjList[edges[i][0]].append(edges[i][1])
            adjList[edges[i][1]].append(edges[i][0])
            print("i={}, adjlist = {}".format(i, adjList))

        for i in range(n):
            if not visited[i]:
                components += 1
                self.dfs(adjList, visited, i)
        return components

    def dfs(self, adjList, visited, startnode):
        visited[startnode] = 1
        print(adjList)
        # print(visited)
        for i in adjList[startnode]:
            # print("i in dfs=",i)
            if not visited[i]:
                self.dfs(adjList, visited, i)


s = Solution()
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
edges1 = [[0,1],[1,2],[0,2],[3,4]]
print(s.countComponents(n, edges1))
