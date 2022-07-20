# https://school.programmers.co.kr/learn/courses/30/lessons/60060
import collections

class Node(object):
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.word = False
        self.children = {}

    def get_key(self):
        return self.key


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
        reversed = full_query.startswith('?')
        if set(full_query) == set('?'):
            answer[-1] += forward_trie[len(full_query)].count
        if not reversed:
            answer[-1] += forward_trie[len(full_query)].starts_with(query)
        if reversed:
            answer[-1] += reverse_trie[len(full_query)].starts_with(query[::-1])
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]	
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]
print(solution(words, queries))