# Minimum Height Trees

## Explain Problem

<https://leetcode.com/problems/minimum-height-trees/>

* Tag
  * DFS
  * BFS
  * Graph
  * Topological Sort
* Acceptable : 38.2%
* Difficulty : Medium

MHT는 트리에서 가장 작은 높이를 가진 트리이다.  
edges를 통해 MHT인 트리를 계산하여 가지들이 제거된 노드들을 출력해야한다.  

```plain
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
```

```plain
Input: s = "00101001", k = 1
Output: 6
Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
The length of this subsequence is 6, so 6 is returned.
```

## Solution

![image](https://velog.velcdn.com/images%2Ftimevoyage%2Fpost%2Fa6908d52-8fef-4b9e-9b04-8f75ea7bc7fe%2F310_trim.png)



```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0] 
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1: newLeaves.append(j)
            leaves = newLeaves
        return leaves
```

* Runtime: 54 ms
* Memory Usage: 13.9 MB

## Reference

<https://velog.io/@timevoyage/leetcode-310-Minimum-Height-Trees>
