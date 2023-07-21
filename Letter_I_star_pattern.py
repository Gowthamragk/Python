n=int(input("Enter:"))
for i in range(n):
  for j in range(n):
    if (i==0 or i==n-1):
      print("*",end=" ")
    elif  (n//2==j):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print( )