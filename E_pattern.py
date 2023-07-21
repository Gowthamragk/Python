n=int(input())
for i in range(n):
  for j in range(n-2):
    if (j==0) :
      print("*",end=" ")
    elif (i==0 or i==n//2 or i==n-1):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print( )
  