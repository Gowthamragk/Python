#common divisor

num1=int(input("Enter the first num"))
num2=int(input("Enter the second num"))
a=[]
if num1>num2:
  for each in range(1,num1//2+2):
    if num1%each==0 and num2%each==0:
      a.append(each)
else:
  for digit in range(1,num2//2):
    if num1%digit==0 and num2%digit==0:
      a.append(digit)
for x in a:
  print(x)
