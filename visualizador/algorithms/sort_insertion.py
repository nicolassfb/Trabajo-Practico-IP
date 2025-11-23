items = []
n = 0
i = 0
j = None

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1
    j = None

def step():
    global items, n, i, j
    done=False
    swap=False
    if i>=n:
        done=True
        return {"done": done}
    if j==None:
        j=i
    a=j-1
    b=j
    if j>0 and items[a]>items[b]:
        aux=items[a]
        items[a]=items[b]
        items[b]=aux
        swap=True
        j-=1
    else:
        i+=1
        j=None
    return {"a": a, "b": b, "swap": swap, "done": done}
