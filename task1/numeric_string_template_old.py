for _ in range(int(input())):
    n=int(input())
    L=list(map(int, input().split()))
    m=int(input())
    for __ in range(m):
        f=1
        d={}
        LL=[]
        S=input()
        if len(S)!=n: print("NO"); continue
        for i in range(n):
            if S[i] not in d.keys(): 
                d[S[i]]=L[i]
                if L[i] in LL: print("NO"); f=0;break
                LL.append(L[i])
            else :
                if d[S[i]] != L[i]: print("NO");f=0;break        
        if f==1:print("YES") 

