def solution(nums):
    number_of_jumps = 0
    current_jump_limit = 0
    reachable_point = 0
    for i in range(len(nums) - 1):
        reachable_point = max(reachable_point, i + nums[i])
        if i == current_jump_limit:
            number_of_jumps += 1
            current_jump_limit = reachable_point
    return number_of_jumps


if __name__ == "__main__":
    print(solution([2, 3, 1, 1, 4]))
