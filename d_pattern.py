n=int(input())
for i in range(n):
  for j in range(n-2):
    if i==0 or i==n-1 or j==0 or j==n-2-1:
      if j==n-2-1 and(i==0 or i==n-1):
        print(" ",end=" ")
      else:
        print("*",end=" ")
    else:
      print(" ",end=" ")
  print( )
