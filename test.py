a1 = [1, 2, 3, 4]
a2 = [11, 22, 33, 44]
a3 = [[1, 11, 111], [2, 22, 222], [3, 33, 333]]
d1 = zip(a1, a2)
d2 = dict(d1)
d3 = dict(zip(a1, a2))
a4 = [(x) for x in a3]
#d5 = dict(a3)
a6 = {n[0]: n[1:] for n in a3}


for x in d1:
    print(x)

z = 10
