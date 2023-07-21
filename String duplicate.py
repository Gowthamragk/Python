sen=input("Enter string:")
x=0
for i in sen:
    
    for j in sen:
        if i==j:
            x+=1
if x>1:
    print("Yes")
else:
    print("No")
