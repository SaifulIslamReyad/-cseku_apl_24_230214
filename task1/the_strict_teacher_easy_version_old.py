for _ in range(int(input())):
    a,b,c=map(int, input().split())
    d,e=map(int, input().split())
    n=int(input())
    if d<n and e<n: print(a-(max(d,e)))
    elif d>n and e>n:  print(min(d,e)-1)
    else: print(abs(d-e)//2)
