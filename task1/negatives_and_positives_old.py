for _ in range(int(input())):
    n=int(input())
    L=list(map(int,input().split()))
    count=0
    for i in range(n):
        if L[i]<0:
            count+=1
            L[i]=-L[i]
    if count%2==0:
        print(sum(L))
    else:
        print(sum(L)-2*min(L))

