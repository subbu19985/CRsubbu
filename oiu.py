bh=int(input())
k=0
lst1=input().split()
lst1=list(map(int,lst))
new=[]
for i in range(0,bh):
    if((lst1.count(lst1[i]))>=2):
      if lst1[i] not in new:
        new.append(lst1[i])
        k=1
if(k==0):
  print("unique")
else:
  for i in range(0,bh):
    print(min(new),end=" ")
    new.remove(min(new))
