# # Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required
# Example 1:
#
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:
#
# Input: intervals = [[7,10],[2,4]]
# Output: 1

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int: