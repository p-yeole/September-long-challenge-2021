#https://www.codechef.com/SEPT21C/problems/TRAVELPS

for _ in range(int(input())):
    nab=list(map(int,input().split()))
    a,b=nab[1],nab[2]
    s=input()
    dic={0:0,1:0}
    ans=0
    for i in s:
        if int(i) in dic:
            dic[int(i)]+=1
        else:
            dic[int(i)]=1
    #for i in s:
    #    if i=='0':
    ans+=dic[0]*a + dic[1]*b
    print(ans)

