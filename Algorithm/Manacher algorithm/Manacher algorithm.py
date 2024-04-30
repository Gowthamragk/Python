word="AMAMBOOBHIJK"

temp_txt="@"+"@".join(word)+"@"
x=[]
for i in range(len(temp_txt)):
    cnt = 0
    t=1
    try:
        while temp_txt[i-t] == temp_txt[i+t]:
            t+=1
            cnt+=1
        x.append(cnt)
    except:
        x.append(cnt)
        
max_ele = x.index(max(x))

res=""
for i in range(max_ele - max(x),max_ele+max(x)+1):
    if temp_txt[i] !="@":
        res +=temp_txt[i]
print(res)