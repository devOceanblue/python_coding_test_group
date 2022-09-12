"""
내부링크, 외부링크, 기본점수를 각각의 페이지별로 가지고있는다

1. 내부링크
{
    a:[b,c],
    b:[a],
    c:[b]
}

2. 외부링크
{
    a:[b],
    b:[a,c],
    c:[a]
}

3. 기본점수
{
    a: 3,
    b: 1,
    c: 1
}

최종점수

    a: 기본점수 + sum([기본점수[i]/len(외부링크[i]) for i in 내부링크[a])

"""
import copy
import re
from collections import defaultdict


def count_word(word, page):
    cnt = 0
    page = page.lower()
    for find in re.findall("[a-zA-Z]+", page):
        if find == word:
            cnt += 1
    return cnt


def solution(word, pages):
    basic_point = defaultdict(int)
    for i in range(len(pages)):
        content = re.search(r'content.*"', pages[i]).group()[9:-1]
        basic_point[content] = count_word(word.lower(), pages[i])

    internal_link = defaultdict(list)
    external_link = defaultdict(list)

    for i in range(len(pages)):
        content = re.search(r'content.*"', pages[i]).group()[9:-1]
        links = re.findall(r'<a href=.*"', pages[i])
        for link in links:
            internal_link[link[9:-1]].append(content)
            external_link[content].append(link[9:-1])

    result = copy.deepcopy(basic_point)

    for key, value in result.items():
        # sum([기본점수[i] / len(외부링크[i]) for i in 내부링크[a])
        result[key] += sum(
            [basic_point[i] / len(external_link[i]) for i in internal_link[key]]
        )

    idx = 0

    result_copy = copy.deepcopy(result)
    for key, value in result_copy.items():
        result[idx] = value
        del result[key]
        idx += 1

    result = dict(sorted(result.items(), key=lambda x: (-x[1], x[0])))
    result = list(result.keys())[0]
