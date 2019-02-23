p,q=map(int,input().split())
l=[]
for val in range(p, q):
  if val>1:
    for n in range(2,val):
      if(val % n) == 0:
        break
    else:
      l.append(val)
for m in range(0,len(l)):
  if(m==len(l)-1):
    print(l[m],end=" ")
  else:
    print(l[m],end=" ")            
