import random as r

"""
ds=[]
total =0
for i in range(50):
    n=r.randrange(0,6)
    print(n,end=" ")
    ds.append(n)

for zzz in range(0,len(ds)):
    total += ds[zzz]
print(total,end="")
"""
# x="123456789"
xx=r.sample(range(1,50),7)
print(xx)