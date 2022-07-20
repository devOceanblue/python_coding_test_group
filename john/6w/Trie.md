# Trie

트라이 구조

![Trie](https://velog.velcdn.com/images%2Fkimdukbae%2Fpost%2F50497c5d-1598-48ad-b7cd-e60b2df366da%2Fimage.png)

* 트리 형태의 자료구조
* 우리가 검색할 때 볼 수 있는 자동완성 기능, 사전 검색 등 문자열을 탐색하는데 특화되어있는 자료구조
* 검색엔진에서 많이 씀

![Trie with python](https://velog.velcdn.com/images%2Fkimdukbae%2Fpost%2F8d819895-5389-4b31-8b6b-a133e4ab3396%2Fimage.png)

```python
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head

        # 삽입할 String 각각의 문자에 대해 자식Node를 만들며 내려간다.
        for char in string:
            # 자식Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            # 같음 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curr_node = curr_node.children[char]

        # 문자열이 끝난 지점의 노드의 data값에 해당 문자열을 표시
        curr_node.data = string


    # 문자열이 존재하는지 탐색!
    def search(self, string):
        # 가장 아래에 있는 노드에서부터 탐색 시작한다.
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        # 탐색이 끝난 후에 해당 노드의 data값이 존재한다면
        # 문자가 포함되어있다는 뜻이다!
        if curr_node.data is not None:
            return True
```

## Problem

2020 KAKAO BLIND RECRUITMENT - 가사 검색
<https://school.programmers.co.kr/learn/courses/30/lessons/60060>

### 필요한 트릭

1. "????????"와 같이 전부 다 물음표일때
2. "ab" + "?"*9998 물음표가 검색하려는 개수보다 많을때
3. 물음표가 맨 앞에 올때랑 뒤에 올때랑 분류
4. 전체 단어를 출력하는 것이 아니라 해당 조건을 만족하는 단어의 개수를 출력

```python
import collections

class Node(object):
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)
        self.count = 0

    def insert(self, string):
        current_node = self.head
        self.count += 1

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
            current_node.count += 1
        current_node.word = True

    def starts_with(self, prefix):
        current_node = self.head

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return 0

        return current_node.count

def solution(words, queries):
    answer = []
    forward_trie = collections.defaultdict(Trie)
    reverse_trie = collections.defaultdict(Trie)
    for word in words:
        forward_trie[len(word)].insert(word)
        reverse_trie[len(word)].insert(word[::-1])

    for full_query in queries:
        answer.append(0)
        query = full_query.replace("?","")
        start = full_query.startswith('?')
        if set(full_query) == set('?'):
            answer[-1] += forward_trie[len(full_query)].count
        if not start:
            answer[-1] += forward_trie[len(full_query)].starts_with(query)
        if start:
            answer[-1] += reverse_trie[len(full_query)].starts_with(query[::-1])
    return answer
```

## others solution

* trie구조를 dictionary를 이용해 품
* 다만... 모수가 조금 더 컸다면, OOM이 발생했을수도 있다고 생각함
  * <https://stackoverflow.com/a/1331541>

```python
def solution(words, queries):
    trie_by_length = [({}, {}) for _ in range(10001)]
    for word in words:
        length = len(word)
        t = trie_by_length[length][0]
        for c in word:
            t['count'] = t.get('count', 0) + 1
            t.setdefault(c, {})
            t = t[c]
        t = trie_by_length[length][1]
        for c in word[::-1]:
            t['count'] = t.get('count', 0) + 1
            t.setdefault(c, {})
            t = t[c]
    ans = []
    for query in queries:
        length = len(query)
        if query[0] == '?':
            t = trie_by_length[length][1]
            query = query[::-1]
        else:
            t = trie_by_length[length][0]
        for c in query:
            if c == '?':
                ans.append(t.get('count', 0))
                break
            if c not in t:
                ans.append(0)
                break
            t = t[c]
    return ans
```

## Reference

<https://velog.io/@kimdukbae/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8A%B8%EB%9D%BC%EC%9D%B4-Trie>
