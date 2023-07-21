#to check num is armstrong or not

n=input()
x=[]
for i in n:
  a=int(i)**len(n)
  x.append(a)
y=sum(x[:])
if y==int(n):
  print("num is armstrong")
else:
  print("num is not an armstrong")