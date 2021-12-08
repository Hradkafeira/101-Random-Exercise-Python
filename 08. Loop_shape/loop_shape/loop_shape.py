def pyramid(n,asc=True):
    if asc:
        for i in range(n):
            yield "\n"+(i+1)*"*"
    else:
        for i in range(n+1,1,-1):
            yield "\n"+(i-1)*"*"

def cube(n):
    for i in range(n):
        if i+1 != n:
            pass
        else:
            for i2 in range(i+1):
                yield "\n"+(i+1)*"*"

print([*pyramid(5,False)])
