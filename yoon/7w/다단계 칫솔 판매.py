import math


class Node:
    def __init__(self, amount=0, parent=None):
        self.amount = amount
        self.parent = parent


def solution(enroll, referral, seller, amount):

    node_dict = {name: Node() for name in enroll}
    root = Node()
    for i in range(len(enroll)):
        if referral[i] == "-":
            node_dict[enroll[i]].parent = root
        else:
            node_dict[enroll[i]].parent = node_dict[referral[i]]

    def recursion(node, amount):
        if node.parent and amount // 10 >= 1:
            give = math.ceil(amount // 10)
            node.amount += amount - give
            recursion(node.parent, give)
        else:
            node.amount += amount

    for i in range(len(seller)):
        recursion(node_dict[seller[i]], amount[i] * 100)

    result = []
    for e in enroll:
        result.append(node_dict[e].amount)
    return result


if __name__ == "__main__":
    a = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    b = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    c = ["young", "john", "tod", "emily", "mary"]
    d = [12, 4, 2, 5, 10]
    print(solution(a, b, c, d))
