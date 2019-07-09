l=input().split()
n=int(l[1])
a1=[int(k) for k in input().split()]
b=sorted(a1)
c=b[::-1]
print(c[n-1])
