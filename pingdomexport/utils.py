# some generic functions that I couldn't find a better place

def intervals(start, end, split_in=3600):
    intervals = []
    while start < end:
        new = end if start + split_in > end else start + split_in
        intervals.append([start, new])
        start = new
    return intervals
