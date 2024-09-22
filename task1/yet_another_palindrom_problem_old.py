for _ in range(int(input())):
    n=int(input());f=0
    L=list(map(int, input().split()))
    for i in range(n-2):
        for j in range(i+2,n):
            if L[i]==L[j]:
                print("YES")
                f=1
                break
        if f==1:break
    if f==0:print('NO')