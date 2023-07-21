n=int(input())
for i in range(n):
  for j in range(n-2):
    if i==0 or i==n-1 or j==0:
      if (i==0 or i==n-1) and j==0:
        print(" ",end=" ")
      else:
        print("*",end=" ")
    else:
      print(" ",end=" ")
  print( )