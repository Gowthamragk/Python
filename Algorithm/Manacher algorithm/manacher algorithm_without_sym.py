word="ABCFBOOBHIJK"
#it can't work the palindroe string in even length
res=""
temp=0
i=1
temp_word=""
while True:
    if temp == len(word)-1:
        break
    try:
        if word[temp -i] == word[temp+i]:
            if i == 1:
                temp_word = word[temp -i] + word[temp]+ word[temp+i]
            else:
                temp_word = word[temp -i] +temp_word +word[temp+i]
            i+=1
        else:
            if len(res) <= len(temp_word):
                res = temp_word
            temp_word=""
            temp +=1
            i=1
    except:
        temp+=1
        continue
    
print(res)