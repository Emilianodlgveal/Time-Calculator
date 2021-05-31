def add_time(start, duration, day=None):
    weekNum = {1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday', 6: 'saturday', 7: 'sunday'}
    weekDays = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}
    minutes = int(start.split(':')[1].split()[0]) + int(duration.split(':')[1])
    hours = int(start.split(':')[0]) + int(duration.split(':')[0])
    if minutes >= 60:
        hours += 1
        minutes -= 60
        n = hours % 12
        if n == 0:
            n = 12
        timeAtEnd = str(n) + ':' + (str(minutes).rjust(2, '0'))
    else:
        n = hours % 12
        if n == 0:
            n = 12
        timeAtEnd = str(n) + ':' + (str(minutes).rjust(2, '0'))

    if 'PM' in start and (hours // 12) % 2 == 1:
        timeAtEnd = timeAtEnd + ' ' + 'AM'
    elif 'PM' in start and (hours // 12) % 2 == 0:
        timeAtEnd = timeAtEnd + ' ' + 'PM'
    elif 'AM' in start and (hours // 12) % 2 == 1:
        timeAtEnd = timeAtEnd + ' ' + 'PM'
    else:
        timeAtEnd = timeAtEnd + ' ' + 'AM'

    rotations = hours // 12
    days = hours // 24

    if day is None:
        if 'PM' in start:
            if rotations % 2 == 1:
                days += 1
                if days == 1:
                    timeAtEnd = timeAtEnd + ' (next day)'
                elif days > 1:
                    timeAtEnd = timeAtEnd + f' ({str(days)} days later)'
            else:
                if days == 1:
                    timeAtEnd = timeAtEnd + ' (next day)'
                elif days > 1:
                    timeAtEnd = timeAtEnd + f' ({str(days)} days later)'
        else:
            if days == 1:
                timeAtEnd = timeAtEnd + ' (next day)'
            elif days > 1:
                timeAtEnd = timeAtEnd + f' ({str(days)} days later)'
        return timeAtEnd
    else:
        if 'PM' in start:
            if rotations % 2 == 1:
                days += 1
                s = str(day).lower()
                finalDay = (weekDays[s] + days) % 7
                if finalDay == 0:
                    finalDay = 7
                if days == 1:
                    timeAtEnd = timeAtEnd + f' {(weekNum[finalDay]).title()} (next day)'
                elif days > 1:
                    timeAtEnd = timeAtEnd + f', {(weekNum[finalDay]).title()} ({str(days)} days later)'
            else:
                s = str(day).lower()
                finalDay = (weekDays[s] + days) % 7
                if finalDay == 0:
                    finalDay = 7
                if days == 1:
                    timeAtEnd = timeAtEnd + f' {(weekNum[finalDay]).title()} (next day)'
                elif days > 1:
                    timeAtEnd = timeAtEnd + f', {(weekNum[finalDay]).title()} ({str(days)} days later)'
                else:
                    return (timeAtEnd + ', ' + (weekNum[finalDay]).title())
        else:
            s = str(day).lower()
            finalDay = (weekDays[s] + days) % 7
            if finalDay == 0:
                finalDay = 7
            if days == 1:
                timeAtEnd = timeAtEnd + f', {(weekNum[finalDay]).title()} (next day)'
            elif days > 1:
                timeAtEnd = timeAtEnd + f', {(weekNum[finalDay]).title()} ({str(days)} days later)'
            else:
                return (timeAtEnd + ', ' + (weekNum[finalDay]).title())
        return (timeAtEnd)


print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "480:43", 'TuesDay'))
