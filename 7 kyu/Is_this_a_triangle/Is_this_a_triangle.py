def is_triangle(a, b, c):
    if a<0 or b<0 or c<0:
        return False
    if b-c<a<b+c and a-c<b<a+c and a-b<c<a+b:
        return True
    else:
        return False