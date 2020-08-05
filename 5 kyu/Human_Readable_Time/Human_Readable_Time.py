def make_readable(seconds):
    def format_readable(n):
        if n < 1:
            return '00'
        else:
            return str(int(n)) if n >= 10 else '0'+ str(int(n))
    hours = seconds / 3600
    minutes = seconds / 60 % 60
    new_seconds = seconds % 60
    return format_readable(hours) + ":" + format_readable(minutes) + ":" + format_readable(new_seconds)
    