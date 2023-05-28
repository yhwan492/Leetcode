# 4. Median of Two Sorted Arrays
# Python
# Time: 67ms
# Memory: 13.5MB
def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    li = nums1 + nums2
    l = len(li)
    li.sort()
    if l % 2 == 1:
        return li[l//2]
    else:
        return (li[l//2]+li[(l//2)-1])/2.0