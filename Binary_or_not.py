n=input("Enter number:")
lst=[]
for i in n:
  i=int(i)
  lst.append(i)
x=0
for cm in lst:
  if cm!=0 and cm!=1:
    x+=1
if x==0:
  print("Binary")
else:
  print("Not Binary")

