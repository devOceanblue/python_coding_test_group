# 6주차

## 문제
 1. [카잉 달력](#카잉-달력)
 2. [토마토](#토마토)
 3. [DSLR](#dslr)
 4. [패션왕 신해빈](#패션왕-신해빈)

### 카잉 달력
- [문재](https://www.acmicpc.net/problem/6064)
- 알고리즘: 탐색, 수학
-  해설
  1. x 에서 N * M까지 반복문을 돌린다.
  2. 초기 k변수를 x로 설정하고 해를 찾을때 까지 N을 더한다.
  3. (k - x) % N == 0 and (k - y) % M == 0 조건 만족 할때 까지 값을 돌린다.
  4. 없는 경우 -1 돌려준다.

- 처음에 제출한 답(실패)
- ```python
    import sys
    input = sys.stdin.readline

    def solution(N, M, x, y):
            k = x
            while k <= N * M:
                    if k % N == x and k % M == y:
                            return k
                    k += N
            return -1

    for _ in range(int(input())):
            N, M, x, y = map(int, input().rstrip().split())
            print(solution(N, M, x, y))
- 이유 처음 K가 x, y 보다 작을 경우가 있음
- 그래서 (k - x) % N == 0 and (k - y) % M == 0 조건으로 찾아야 한다.
- ``` python
    import sys
    input = sys.stdin.readline

    def solution(N, M, x, y):
            k = x
            while k <= N * M:
                    if (k - x) % N == 0 and (k - y) % M == 0:
                            return k
                    k += N
            return -1

    for _ in range(int(input())):
            N, M, x, y = map(int, input().rstrip().split())
            print(solution(N, M, x, y))

### 토마토
- [문제](https://www.acmicpc.net/problem/7569)
- 알고리즘: 시뮬레이션, DFS
- 해설
  1. x, y, z축이 있는 3차원 배열 이다.
  2. 앞, 뒤, 오른쪽, 왼쪽, 위, 아래 방향 설정 한다.
  3. 탐색하면서 0인것을 찾으면 탐색한 위치값은  기존 위치 값에 +1하면서 저장한다.
  4. 탐색이 완료되면 0인것 부터 찾고 없으면 최대 값 -1로 리턴한다.
- 코드  
  - ```python
    import sys
    from collections import deque
    input = sys.stdin.readline

    def solution(boxs, location):
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        dz = [-1, 1]
        days = 0
        queue = location
        
        while queue:
            z, y, x = queue.popleft()
            value = boxs[z][y][x]

            for i in range(4):
                fx = x + dx[i]
                fy = y + dy[i]
                if 0 <= fx < N and 0 <= fy < M and boxs[z][fy][fx] == 0:
                    boxs[z][fy][fx] = value + 1
                    queue.append((z, fy, fx))
            
            for i in range(2):
                fz = z + dz[i]
                if 0 <= fz < H and boxs[fz][y][x] == 0:
                    boxs[fz][y][x] = value + 1
                    queue.append((fz, y, x))
        
        max_value = 0
        
        for box in boxs:
            for row in box:
                if 0 in row: return -1
                now_max_value = max(row)
                if max_value < now_max_value:
                    max_value = now_max_value
                    
        return max_value - 1

    N, M, H = map(int, input().split())
    tensor = []
    location = deque([])

    for z in range(H):
        metrix = []
        for y in range(M):
            vector = list(map(int, input().split()))
            for x, value in enumerate(vector):
                if value == 1:
                    location.append((z, y, x))
            metrix.append(vector)
        tensor.append(metrix)
        
    print(solution(tensor, location))

### DSLR
- [문제](https://www.acmicpc.net/problem/9019)
- 알고리즘: 문자열, 수학, DFS
- 해설
  1. D, S, L, R 명령어를 사용해서 원하는 숫자를 찾는 것이다.
  2. 0~ 10000까지 배열을 만들고 각 명령어 연산후 그 다음에는 탐색 하지 못하도록 한다.
  3. 명령어 연산후 10000나머지를 한다.
  4. 쉬프트 연산일때 4자리수가 아니면 비어있는 자리를 0으로 채운다.
  5. 왼쪽 이동 연산은 4자리 미만은 10을 곱하고 4자리 일때는 나머지 1000에서 곱하기 10을 하고 앞자리는 1000을 나눠서 몫에 값에 뒤에 더한다.
  6. 오른쪽 이동 연산은 10을 나눠서 몫 + 나머지 * 1000을 한다.
  7. 제출은 python3말고 pypy로 제출한다.
- 코드  
  - ```python
    from collections import deque
    import sys

    def solution(x, y):
        visited = [True] * 10000
        visited[x] = False
        queue = deque([(x, '')])
        while queue:
            num, path = queue.popleft()
            if num == y:
                return path
            
            length = len(str(num))
            
            value = (num * 2) % 10000
            if visited[value]:
                visited[value] = False
                queue.append((value, path + "D"))
                
            value = (num - 1) % 10000
            if visited[value]:
                visited[value] = False
                queue.append((value, path + "S"))
                
            if length < 4:
                value = num * 10
            else:
                value = (num % 1000) * 10 + num // 1000
            if visited[value]:
                visited[value] = False
                queue.append((value, path + "L"))
                
            value = (num % 10) * 1000 +  num // 10
                    
            if visited[value]:
                visited[value] = False
                queue.append((value, path + "R"))

    input = sys.stdin.readline

    for _ in range(int(input())):
        A, B= map(int, input().split())
        print(solution(A, B))

### 패션왕 신해빈