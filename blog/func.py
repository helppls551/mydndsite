def dex(dext,bol):
    dext = int(dext)
    if bol:
        if dext >= 5:
            return 5 + 2
        elif dext / 4 >= 4.5:
            return 4 + 2
        elif dext / 4 >= 4:
            return 3 + 2
        elif dext / 4 >= 3.5:
            return 2 + 2
        elif dext / 4 >= 3:
            return 1 + 2
        elif dext / 4 >= 2.5:
            return 0 + 2
        elif dext / 4 >= 2:
            return -1 + 2
        elif dext / 4 >= 1.5:
            return -2 + 2
        elif dext / 4 >= 1:
            return -3 + 2
        elif dext / 4 >= 0.5:
            return -4 + 2
        elif dext / 4 >= 0:
            return -5 + 2
    else:
        if dext >= 5:
            return 5
        elif dext / 4 >= 4.5:
            return 4
        elif dext / 4 >= 4:
            return 3
        elif dext / 4 >= 3.5:
            return 2
        elif dext / 4 >= 3:
            return 1
        elif dext / 4 >= 2.5:
            return 0
        elif dext / 4 >= 2:
            return -1
        elif dext / 4 >= 1.5:
            return -2
        elif dext / 4 >= 1:
            return -3
        elif dext / 4 >= 0.5:
            return -4
        elif dext / 4 >= 0:
            return -5
