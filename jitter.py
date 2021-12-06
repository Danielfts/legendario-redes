path = input('Ingrese la ruta del archivo csv:\n')

f = open(path)
l = []
p = [45 ,58, 130, 65] 
delta = 0
n = 0
m = 0

for i in f:
    l.append(float(i))
    # print(i)
# l = p
for j in range(len(l)-1):
    d = l[j+1]-l[j]
    # print(d)
    delta += d

# print(l)
# print(delta)
jitter = delta / (len(l)-1)
print(jitter)