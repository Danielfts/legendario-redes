path = input('Ingrese la ruta del archivo csv:\n')
f = open(path)
l = []
delta = 0
for i in f:
    l.append(float(i))
for j in range(len(l)-1):
    d = l[j+1]-l[j]
    # print(d)
    delta += d
jitter = delta / (len(l)-1)
print(jitter)