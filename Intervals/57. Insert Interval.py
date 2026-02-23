def insert(intervals, newInterval):
    res = []
    i = 0
    n = len(intervals)
    new_start, new_end = newInterval
    
    # Phase 1: Add all intervals that end before the new interval starts
    while i < n and intervals[i][1] < new_start:
        res.append(intervals[i])
        i += 1
        
    # Phase 2: Merge overlapping intervals
    while i < n and intervals[i][0] <= new_end:
        new_start = min(new_start, intervals[i][0])
        new_end = max(new_end, intervals[i][1])
        i += 1
    res.append([new_start, new_end])
    
    # Phase 3: Add the remaining intervals
    while i < n:
        res.append(intervals[i])
        i += 1
        
    return res


print(insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))