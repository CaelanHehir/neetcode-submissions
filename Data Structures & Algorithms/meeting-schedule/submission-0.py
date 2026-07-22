"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def check_overlap(self, meeting1: Interval, meeting2: Interval) -> bool:
        return (meeting1.start <= meeting2.start < meeting1.end) or (meeting2.start <= meeting1.start < meeting2.end)

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        assignments = []
        for meeting in intervals:
            if all(not self.check_overlap(meeting, room_meeting)
                   for room_meeting in assignments):
                assignments.append(meeting)
            else:
                return False
        return True
