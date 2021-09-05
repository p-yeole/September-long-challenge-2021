#https://www.codechef.com/SEPT21C/problems/SHUFFLIN

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    odd_elements,even_elements=0,0
    #odd_pos,even_pos=0,0
    ans=0
    for i in a:
        if i%2==0:
            even_elements+=1
        else:
            odd_elements+=1
    if n%2==0:
        odd_pos,even_pos=n//2,n//2
    else:
        odd_pos,even_pos= (n//2) +1,n//2

    if odd_pos<=even_elements:
        ans+=odd_pos
    elif odd_pos>even_elements:
        ans+=even_elements 
    if even_pos<=odd_elements:
        ans+=even_pos 
    elif even_pos>odd_elements:
        ans+= odd_elements 
    print(ans)