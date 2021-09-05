#https://www.codechef.com/SEPT21C/problems/AIRLINE

for _ in range(int(input())):
    arr=list(map(int,input().split()))
    a,b,c,d,e=arr[0],arr[1],arr[2],arr[3],arr[4]
    l=sorted(arr[:3],reverse=True)
    a,b,c=l[0],l[1],l[2]
    if a<=e:
        if b+c<=d:
            print('YES')
        else:
            print('NO')
    elif b<=e:
        if a+c<=d:
            print('YES')
        else:
            print('NO')
    elif c<=e:
        if a+b<=d:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')