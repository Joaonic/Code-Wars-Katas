def bouncing_ball(h, bounce, window):
    if h > 0 and  0 < bounce < 1 and window < h:
        cont = 0
        while h > window:
            h = h * bounce
            print(h)
            cont += 2
        return cont - 1
    return -1