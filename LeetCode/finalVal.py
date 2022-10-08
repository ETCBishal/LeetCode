def findFinalValue(nums, original):
    """
    :type nums: List[int]
    :type original: int
    :rtype: int
    """
    lookup = set(nums)
    print(lookup)
    while original in lookup:
        original *= 2
    return original


soln =findFinalValue([2,3,6,12,24],3)
print(soln)