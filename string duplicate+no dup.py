def gen(string):
    if len(string) == 1:
        return string + "1"
    count = 1
    while string[count] == string[0]:
        count += 1
    return (string[0]+str(count))*count +gen(string[count:])

gen("neelu")