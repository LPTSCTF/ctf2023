with open("cfile") as challenge:
    best = 0
    for i in challenge.readlines():
        t = 1
        for i in i.split(" "):
            t *= int(i)
        if t > best: best = t
        t = 0
    print(best)