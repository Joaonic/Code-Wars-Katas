def fake_bin(x):
    return ''.join(['0' if int(n) < 5 else '1' for n in list(x)])