items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, n, i, j
    a=j
    b=j+1
    if items[a]>items[b]:
        aux=items[a]
        items[a]=items[b]
        items[b]=aux
        swap=True
    else:
        swap=False
    j+=1
    if j>=n-1-i:
        j=0
        i+=1
    if i==n-1:
        done=True
    else:
        done=False
    return {"a": a, "b": b, "swap": swap, "done": done}
