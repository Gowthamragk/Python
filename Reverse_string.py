n=input("Enter number:")
lst=[]
for i in n:
  lst.append(i)
length=len(lst)
for i in range(length // 2):
        lst[i], lst[length - i-1] = lst[length - i-1], lst[i]
print(lst)