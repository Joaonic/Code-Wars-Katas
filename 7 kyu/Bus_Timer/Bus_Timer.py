def bus_timer(current_time):
    hh, mm = map(int, current_time.split(':'))
    if mm >= 60 or hh >= 24:
        return False
    if 0 <= hh < 6:
        i = 355 - (hh * 60 + mm)
        if i<0:
            return 15 + i
        else:
            return i
    if hh == 23 and mm > 55:
        return 355 +(60 - mm)
    if mm <= 10:
        return 10 - mm
    if 10 < mm <= 25:
        return 25 - mm
    if 25 < mm <= 40:
        return 40 - mm
    if 40 < mm <= 55:
        return 55 - mm
    if 55 < mm < 60:
        return 70 - mm