def permutations(text, length, result):
    if length == 0:
        list_result.append(result[:])
        return

    for char in text:
        if char not in result:
            permutations(text, length-1, result + [char])
    

string = input("enter the string : ")
permutations_library = {}
for i in range(1, len(string)+1):
    list_result = []
    permutations(string, i, [])
    permutations_library[f"{i} length permutations"] = list_result


print(permutations_library)
  
