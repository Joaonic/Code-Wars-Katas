import re
def highlight(code):
    def translate(match):
        char = match.group(0)
        if 'F' == char[0] :
            return '<span style="color: pink">%s</span>' % char
        if 'L' == char[0] :
            return '<span style="color: red">%s</span>' % char
        if 'R' == char[0] :
            return '<span style="color: green">%s</span>' % char
        if char.isdigit() :
            return '<span style="color: orange">%s</span>' % char
        return char
    return re.sub(r'\d+|(.)\1*', translate, code)