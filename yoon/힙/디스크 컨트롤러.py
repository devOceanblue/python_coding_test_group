def solution(jobs):
    cur_time = 0
    cur_history = []
    jobs.sort(key=lambda x: (x[0], x[1] - x[0]))
    while jobs:
        next_list = sorted([i for i in jobs if i[0] <= cur_time], key=lambda x: (x[1]))
        if not next_list:
            next = jobs[0]
            cur_time = jobs[0][0]
        else:
            next = next_list[0]
        cur_time += next[1]
        cur_history.append([next[0], cur_time])
        jobs.remove(next)
    result = sum([x[1] - x[0] for x in cur_history]) // len(cur_history)
    return result


if __name__ == "__main__":
    print(solution([[0, 5], [1, 2], [5, 5]]))
