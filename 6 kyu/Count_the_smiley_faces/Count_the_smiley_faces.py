def count_smileys(arr):
    dic = {':-)',':-D',':~)',':~D',';-)',';-D',';~)',';~D', ':)',':D',';)',';D'}
    cont = 0
    for smile in arr:
        if smile in dic:
            cont += 1
    return cont