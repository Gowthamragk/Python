#to find it is a perfect number
n=int(input())
x=0
for i in range(1,n//2+2):
  if n%i==0:
    x+=i
if x==n:
  print("perfect")
else:
  print("not perfect")