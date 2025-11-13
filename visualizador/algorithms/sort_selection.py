items = []
n = 0
i = 0
j = 0
min_idx = 0
fase = "buscar"
def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase
    swap=False
    done=False
    if fase=="buscar":
        if j<n:
            if items[j]<items[min_idx]:
                min_idx=j
            j+=1
        else:
            fase="swap"
    if fase=="swap":
        if i<n:
            if min_idx!=i:
                aux=items[min_idx]
                items[min_idx]=items[i]
                items[i]=aux
                swap=True
            i+=1
            j=i+1
            min_idx=i
        if i==n:
            done=True
        else:
            fase = "buscar"
    return {"a": min_idx, "b": i, "swap": swap, "done": done}

