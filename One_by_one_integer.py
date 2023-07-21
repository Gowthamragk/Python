num=int(input("Enter:"))
digits=[]
while num > 0:
   digit = num % 10
   digits.append(digit)
   num //= 10
for digit in reversed(digits):
            print(digit)