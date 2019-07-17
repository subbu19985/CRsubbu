x,y=input().split()
a=abs(len(y)-len(x))
for i in range(len(x)):
    if(len(y)==1 and y[i] in x):
        break
    if(x[i]!=y[i]):
        a=a+1
print(a)
