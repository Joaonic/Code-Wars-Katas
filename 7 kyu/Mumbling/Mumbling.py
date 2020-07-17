def accum(s):
    ans = ''
    for i in range(len(s)):
        for n in range(i+1):
            if n == 0:
                ans += s[i].upper()
            else:
                ans += s[i].lower()
        ans += '-'
    return ans[:len(ans)-1]