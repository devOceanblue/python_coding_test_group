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


if __name__ == "__main__":
    # assert solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]) == 1
    print(
        re.findall(
            '<a href="https:.\S"', '<a href="https://b.c./rerfdb" test="dfgsfdqom">'
        )
    )
    # print(count_word('muzi', 'con%    muzI92apeach'))
    # print(count_word('aba', 'aba@aba aba'))
    # print(count_word('muzi', '%muzimuzi!#'))
