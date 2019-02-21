from random import randint
from collections import namedtuple

# Given a list of meeting objects (e.g. {name:
# 'MeetingName', hours: numHours}) and an integer
# haveHours denoting how many hours of one's schedule
# alloted to meetings, write a function that
# optimizes the total number of meetings in one's day


Candidate = namedtuple('Candidate', ['residual_time', 'meetings'])

class Meeting:

    def __init__(self, name, minutes):
        self.name = name
        self.minutes = minutes

    def __repr__(self):
        return "<" + self.name + ", " + str(self.minutes) + "m>"


def scheduleMostMeetings(meetings, total_minutes):
    if total_minutes <= 0:
        return []

    if meetings == []:
        return []

    if len(meetings) == 1 and meetings[0].minutes > total_minutes:
        return []

    if len(meetings) == 1 and meetings[0].minutes <= total_minutes:
        return meetings

    shorter = []
    total_shorter_mins = 0
    longer = []

    for meeting in meetings:
        if meeting.minutes < meetings[0].minutes:
            shorter += [meeting]
            total_shorter_mins += meeting.minutes
        elif meeting.minutes > meetings[0].minutes:
            longer += [meeting]

    return scheduleMostMeetings(shorter, total_minutes) + \
           scheduleMostMeetings([meetings[0]], total_minutes - total_shorter_mins) + \
           scheduleMostMeetings(longer, total_minutes - total_shorter_mins - meetings[0].minutes)


# 2) Using the same input, write a function that optimizes the total number of hours one spends in meetings

def minutes_optimization(meetings, total_minutes):
    
    if meetings == []:
        return Candidate(total_minutes, [])

    if total_minutes <= 0:
        return Candidate(0, [])

    if len(meetings) == 1 and meetings[0].minutes > total_minutes:
        return Candidate(total_minutes, [])

    if len(meetings) == 1 and meetings[0].minutes <= total_minutes:
        return Candidate(total_minutes - meetings[0].minutes, meetings)

    candidates = []
    for i, m in enumerate(meetings):

        diff = total_minutes - m.minutes
        if diff < 0:
            continue
        temp = minutes_optimization(meetings[i+1:], diff)
        candidates += [Candidate(temp[0], [m]+temp[1])]

    if len(candidates) == 0:
        return Candidate(total_minutes, [])
    else:
        min_diff = min([c.residual_time for c in candidates if c.residual_time >= 0])

        return Candidate(min_diff, [c.meetings for c in candidates if c.residual_time == min_diff][0])


if __name__ == '__main__':

    total_time = 1 * 40
    num_meetings = 5

    meetings = [Meeting("Meeting" + str(i), randint(7, 15)) for i in range(num_meetings)]

    # print(meetings)

    calendar = scheduleMostMeetings(meetings, total_time)

    # print(len(calendar))

    result = minutes_optimization(meetings, total_time)

    print(meetings)
    print(sum([m.minutes for m in result.meetings]))
    print("Residual time: ", result.residual_time)
    print(result)
