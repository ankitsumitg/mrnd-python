def get_hcf(a,b):
    ans = []
    for i in a:
        for j in b:
            x1,y1 = i
            x2,y2 = j
            if x1 == x2:
                ans.append((x1,y1 if y1 < y2 else y2))
    return ans


def get_lcm(a,b):
    c = {}
    for i in a:
        x,y = i
        c[x] = y
    for i in b:
        x,y = i
        if x in c:
            c[x] = y if y > c[x] else c[x]
        else:
            c[x] = y
    return sorted(list(c.items()))


def multiply(a,b):
    c = {}
    for i in a:
        x, y = i
        c[ x ] = y
    for i in b:
        x, y = i
        if x in c:
            c[ x ] = y + c[ x ]
        else:
            c[ x ] = y
    return sorted(list(c.items()))