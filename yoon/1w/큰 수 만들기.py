def solution(number, k):
    number = list(number)

    max_num = float("-inf")

    def dfs(nums, depth):
        nonlocal max_num
        if depth == k:
            max_num = max(max_num, int("".join(nums)))
            return

        for num in nums:
            next_nums = nums[:]
            next_nums.remove(num)
            dfs(next_nums, depth + 1)

    dfs(number, 0)
    return max_num


if __name__ == "__main__":
    print(solution("1924", 2))
