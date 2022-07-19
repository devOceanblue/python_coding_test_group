def solution(height):
    i, j = 0, len(height) - 1
    max_left = max_right = result = 0

    while i < j:
        max_left, max_right = max(max_left, height[i]), max(max_right, height[j])
        min_max = min(max_left, max_right)
        result += max(min_max - height[i], 0) + max(min_max - height[j], 0)
        if max_left < max_right:
            i += 1
        elif max_left >= max_right:
            j -= 1
    return result


if __name__ == "__main__":
    print(solution(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
