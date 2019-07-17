from itertools import combinations
strin,num=map(int,input().split())
c=len(str(strin))
S=list(combinations(str(strin),c-num))
S=(sorted(S))
y="".join(S[0])
print(y)
