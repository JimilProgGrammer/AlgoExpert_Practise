# Time: O(C1 + C2); Space: O(C1 + C2)
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
    updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)
    mergedCalendar = mergeCalendars(updatedCalendar1, updatedCalendar2)
    flattenedCalendar = flattenCalendar(mergedCalendar)
    return getMatchingAvailabilities(flattenCalendar, meetingDuration)

def updateCalendar(calendar, dailyBounds):
    # Make a copy of the inputs so that you don't mutate
    # the original input values.
    updatedCalendar = calendar[:]
    updatedCalendar.insert(0, ["0:00", dailyBounds[0]])
    updatedCalendar.append([dailyBounds[1], "23:59"])
    # Convert time in string to numeric form (no of minutes)
    return list(map(lambda m: [timeToMinutes(m[0]), timeToMinutes(m[1])], updatedCalendar))

def timeToMinutes(time):
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes

def mergeCalendars(calendar1, calendar2):
    merged = []
    i, j = 0,0
    while i < len(calendar1) and j < len(calendar2):
        meeting1, meeting2 = calendar1[i], calendar2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1
    
    while i < len(calendar1):
        merged.append(calendar1[i])
        i += 1
    while j < len(calendar2):
        merged.append(calendar2[j])
        j += 1
    return merged

def flattenCalendar(calendar):
    flattened = [calendar[0][:]]
    for i in range(1, len(calendar)):
        # Current meeting that you are iterating
        currentMeeting = calendar[i]
        # The last meeting that was appended in the flattened array
        previousMeeting = flattened[-1]
        currentStart, currentEnd = currentMeeting
        previousStart, previousEnd = previousMeeting
        if previousEnd >= currentStart:
            newPreviousMeeting = [previousStart, max(previousEnd, currentEnd)]
            flattened[-1] = newPreviousMeeting
        else:
            flattened.append(currentMeeting[:])
    return flattened

def getMatchingAvailabilities(calendar, meetingDuration):
    matchingAvailabilities = []
    for i in range(1, len(calendar)):
        startTime = calendar[i-1][1]
        endTime = calendar[i][0]
        availabilityDuration = endTime - startTime
        if availabilityDuration >= meetingDuration:
            matchingAvailabilities.append([startTime, endTime])
    return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])], matchingAvailabilities))

def minutesToTime(minutes):
    # rounding down with "//"
    hours = minutes // 60
    mins = minutes % 60
    hoursString = '0' + str(hours) if hours < 10 else str(hours)
    minsString = '0' + str(mins) if mins < 10 else str(mins)
    return hoursString + ":" + minsString
