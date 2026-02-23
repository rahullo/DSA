def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    print("Intervals: ", intervals)
    merged = []
    
    for interval in intervals:
        # If the list is empty or there is no overlap
        if not merged or interval[0] > merged[-1][1]:
            print("If: ", interval)
            merged.append(interval)
        else:
            print("Else: ", interval)

            # There is an overlap, so merge the current interval 
            # with the previous one by updating the end time
            merged[-1][1] = max(merged[-1][1], interval[1])
            
    return merged



print(merge([[1,3],[2,6],[8,10],[15,18]]))