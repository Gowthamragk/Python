x=int(input("Enter first"))
y=int(input("enter second"))
if(x==y):
    z =x <<1
    print(z)
else:
    tem=(x&y)
    carry=x|y
    z=(tem^carry) <<1
    w= z<<1
    print(tem)
    print(carry)
    print(w)
