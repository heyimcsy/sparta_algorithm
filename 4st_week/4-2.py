def max_meetings(meetings):
    sorted_meetings = sorted(meetings, key=lambda x: x[1])

    count = 0
    last_end_time = -1

    for start, end in sorted_meetings:

        if start >= last_end_time:
            count += 1
            last_end_time = end

    return count


meetings = [(0, 6), (1, 4), (3, 5), (3, 8), (5, 7), (8, 9)]
print(max_meetings(meetings))