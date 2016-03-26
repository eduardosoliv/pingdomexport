# some generic functions that I couldn't find a better place

# strangely pingom doesn't seem to respect well the intervals
# from               to                 number of results
# 1458372621         1458372621 + 3600  116
# 1458372621 + 3600  1458372621 + 7200  120
def intervals(start, end, split_in=3600):
    intervals = []
    while start < end:
        new = end if start + split_in > end else start + split_in
        intervals.append([start, new])
        start = new
    return intervals
