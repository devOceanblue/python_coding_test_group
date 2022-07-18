# https://school.programmers.co.kr/learn/courses/30/lessons/17676
import heapq
import datetime
import time

def datetime_to_timestamp(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000.0

def solution(lines):
    answer = 0
    stack = list()
    for _ in range(len(lines)):
        end_date_str, end_time_str, duration_str = lines.pop().split()
        end_time = datetime.datetime.fromisoformat(f'{end_date_str} {end_time_str}')
        duration = datetime.timedelta(seconds=(float(duration_str[:-1]) - 0.001))
        start_time = ( end_time - duration )
        while stack and -stack[0] >= datetime_to_timestamp(end_time) + 1000:
            heapq.heappop(stack)
        heapq.heappush(stack,-datetime_to_timestamp(start_time))
        answer = max(answer, len(stack))
    return answer