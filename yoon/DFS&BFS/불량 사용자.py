from itertools import permutations


def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    users = list(permutations(user_id, len(banned_id)))
    result = []

    for users in users:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in result:
                result.append(users)

    return len(result)


if __name__ == "__main__":
    print(
        solution(
            ["frodo", "fradi", "crodo", "abc123", "frodoc"],
            ["*rodo", "*rodo", "******"],
        )
    )
