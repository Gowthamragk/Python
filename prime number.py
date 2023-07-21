n=int(input("Enter the number"))
x=0
if n==1:
    print(n,"is not prime number")
else:
    for i in range(2,n):
        if n%i==0:
            x+=1
        
if x>0:
    print("Not prime number")
else:
    print("prime number")
