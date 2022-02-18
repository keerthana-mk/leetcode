# https://leetcode.com/problems/graph-valid-tree/
# Graph Valid Tree
#
# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge
# between nodes ai and bi in the graph.
# Return true if the edges of the given graph make up a valid tree, and false otherwise.
#
# Example 1:
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true
#
# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
from collections import OrderedDict


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adjList = [[] for i in range(n)]
        visited =set()
        for i in range(len(edges)):
            adjList[edges[i][0]].append(edges[i][1])
            adjList[edges[i][1]].append(edges[i][0])
        # print(adjList)
        self.dfs(adjList, 0,visited)
        # print(visited)
        return len(visited) ==n


    def dfs(self,adjList, startnode,visited):
        # print(startnode)
        if startnode in visited:
            return
        visited.add(startnode)
        for i in adjList[startnode]:
            self.dfs(adjList,i,visited)
s = Solution()
n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
edges1 = [[0,1],[1,2],[2,3],[1,3],[1,4]]

print(s.validTree(n,edges))