def tribonacci(signature, n):
    if n < 3:
        return signature[:n]
    else:
        ans = signature
        [ans.append(sum(signature[i:i+3])) for i in range(n-3)]
        return ans