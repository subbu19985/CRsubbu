subbu,ganesan=map(str,input().split())
y1=0
if(len(subbu)>len(ganesan)):
  subbu,ganesan=ganesan,subbu
z=0
while(z<len(subbu)):
  y1+=(ord(ganesan[z])-ord(subbu[z]))
  z+=1
for z in range(z,len(ganesan)):
  y1+=ord(ganesan[z])-ord('a')+1
print(y1)
