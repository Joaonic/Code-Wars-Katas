def parts_sums(ls):
    ans = [sum(ls)]
    for i in range(len(ls)):
        ans.append(ans[i] - ls[i])
    return ans