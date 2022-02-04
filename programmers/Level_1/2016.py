import datetime


def solution(a, b):
    answer = ''
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    date = datetime.date(2016, a, b)
    answer = day[date.weekday()]
    return answer
