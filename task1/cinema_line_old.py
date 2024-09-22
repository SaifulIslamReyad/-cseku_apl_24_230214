input()
a=b=0
L=list(map(int, input().split()))
for i in L:
    if i==25:
        a+=1
    elif i==50:
        b+=1
        a-=1
    elif i==100:
        if b>0:
            b-=1
            a-=1
        else:
            a-=3
    if a<0 or b<0:
        print("NO");exit()
print("YES")
